from dataclasses import dataclass, asdict
from typing import Optional, Union, List, Dict

from seeq.spy import _common, _login
from seeq.spy._errors import SPyValueError, SPyRuntimeError
from seeq.spy._session import Session
from seeq.spy._status import Status

SEND_EMAIL_ENDPOINT = '/notify/sendEmail'


@dataclass(frozen=True)
class EmailRecipient:
    email: str
    name: Optional[str] = None

    def __post_init__(self):
        if not _common.is_email(self.email):
            raise SPyValueError(f"Invalid email address provided: {self.email}")


@dataclass(frozen=True)
class EmailAttachment:
    """
    The dataclass for email attachments.

    Attributes:
        content (str): The base64 encoded content of the attachment
        type (str): The MIME type of the attachment
        filename (str): The filename for the attachment
    """
    content: str
    type: str
    filename: str

    def __post_init__(self):
        if not self.content or self.content.isspace():
            raise SPyValueError(f"A non-blank attachment content must be provided")
        if not self.type or self.type.isspace():
            raise SPyValueError(f"A non-blank attachment type must be provided")
        if not self.filename or self.filename.isspace():
            raise SPyValueError(f"A non-blank attachment filename must be provided")


@dataclass(frozen=True)
class EmailRequestInput:
    toEmails: List[EmailRecipient]
    subject: str
    content: str
    ccEmails: Optional[List[EmailRecipient]] = None
    bccEmails: Optional[List[EmailRecipient]] = None
    attachments: Optional[List[EmailAttachment]] = None

    def __post_init__(self):
        if len(self.toEmails) < 1:
            raise SPyValueError(f"At least one recipient needs to be provided")
        if not self.subject or self.subject.isspace():
            raise SPyValueError(f"A non blank subject must be provided")
        if not self.content or self.content.isspace():
            raise SPyValueError(f"A non blank content must be provided")

    def to_dict(self) -> Dict:
        return asdict(self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})


RecipientType = Union[str, EmailRecipient, List[Union[str, EmailRecipient]]]
AttachmentType = Union[EmailAttachment, List[EmailAttachment]]


def _create_email_request_input(to: RecipientType, subject: str, content: str,
                                cc: Optional[RecipientType], bcc: Optional[RecipientType],
                                attachments: Optional[AttachmentType]) -> EmailRequestInput:
    def standardize_recipient_list(recipients: Optional[RecipientType]) -> Optional[List[EmailRecipient]]:
        if recipients is None:
            return None
        if isinstance(recipients, str):
            return [EmailRecipient(email=recipients)]
        if isinstance(recipients, EmailRecipient):
            return [recipients]
        if isinstance(recipients, List):
            return [recipient if isinstance(recipient, EmailRecipient) else EmailRecipient(email=recipient)
                    for recipient in recipients if isinstance(recipient, str) or isinstance(recipient, EmailRecipient)]

    def standardize_attachments_list(attachments_list: Optional[AttachmentType]) -> Optional[List[EmailAttachment]]:
        if attachments_list is None:
            return None
        if isinstance(attachments_list, EmailAttachment):
            return [attachments_list]
        if isinstance(attachments_list, List):
            return attachments_list

    to = standardize_recipient_list(to)
    cc = standardize_recipient_list(cc)
    bcc = standardize_recipient_list(bcc)
    attachments = standardize_attachments_list(attachments)
    return EmailRequestInput(toEmails=to, subject=subject, content=content, ccEmails=cc, bccEmails=bcc,
                             attachments=attachments)


def _call_send_email_api(session: Session, email_body: EmailRequestInput) -> None:
    api_client_url: str = session.private_url
    send_email_request_url: str = api_client_url + SEND_EMAIL_ENDPOINT

    email_request_body_json = email_body.to_dict()
    response = session.requests.post(send_email_request_url,
                                     headers={
                                         "Content-Type": "application/vnd.seeq.v1+json",
                                         "Accept": "application/vnd.seeq.v1+json",
                                     },
                                     json=email_request_body_json
                                     )
    if response.status_code != 202:
        raise SPyRuntimeError(f"Your message could not be sent.\n"
                              f"Response code: {response.status_code}\n"
                              f"Response content: {response.content}")


def send_email(to: RecipientType, subject: str, content: str, *,
               cc: Optional[RecipientType] = None, bcc: Optional[RecipientType] = None,
               attachments: Optional[AttachmentType] = None, errors: Optional[str] = None,
               quiet: bool = False, status: Optional[Status] = None, session: Optional[Session] = None) -> None:
    """
    Sends an email notification.
    The number of recipients (to + cc + bcc) cannot be greater than 50 to avoid spam. This
    limit may vary depending on the system configuration.
    The email sending is rate limited per user and per Seeq server.

    Parameters
    ----------
    to : str, EmailRecipient, List[str or EmailRecipient]
        The email recipients list. It is mandatory to have at least one recipient.

    subject : str
        The email subject, mandatory value.

    content : str
        The email content, mandatory value. The content supports basic HTML tags.

    cc : str, EmailRecipient, List[str or EmailRecipient], default None
        Carbon Copy recipients list

    bcc : str, EmailRecipient, List[str or EmailRecipient], default None
        Blank Carbon Copy recipients list

    attachments : EmailAttachment, List[EmailAttachment], default None
        Attachments to be sent with the email.

    errors : {'raise', 'catalog'}, default 'raise'
        If 'raise', any errors encountered will cause an exception. If
        'catalog', errors will be added to a 'Result' column in the status.df
        DataFrame.

    quiet : bool, default False
        If True, suppresses output. Note that when status is provided,
        the quiet setting of the Status object that is passed in takes precedent.

    status : spy.Status, optional
        If specified, the supplied Status object will be updated as the command
        progresses. It gets filled in with the same information you would see
        in Jupyter in the blue/green/red table below your code while the
        command is executed. The table itself is accessible as a DataFrame via
        the status.df property.

    session : spy.Session, optional
        If supplied, the Session object (and its Options) will be used to
        store the login session state. This is useful to log in to different
        Seeq servers at the same time or with different credentials.


    Examples
    --------
    Simple usage:

    >>> spy.notifications.send_email('test@seeq.com', 'Subject', 'Content')

    A more complex example:

    >>> from seeq.spy.notifications import send_email, EmailRecipient
    >>> send_email(to=[
    >>>                 'test@seeq.com',
    >>>                 EmailRecipient(name='Test Name', email='test.name@seeq.com')
    >>>               ],
    >>>            cc="some_user@seeq.com",
    >>>            bcc=['bcc.recipient@seeq.com', 'another.bcc@seeq.com'],
    >>>            subject='Subject',
    >>>            content='Email content')

    An example with an attachment:

    >>> import base64
    >>> from seeq.spy.notifications import send_email, EmailAttachment
    >>> send_email(to="test@seeq.com",
    >>>            subject="Email with attachment",
    >>>            content="See attachment",
    >>>            attachments=EmailAttachment(content=base64.b64encode(b"My message attachment").decode("ascii"),
    >>>                                        type="text/plain",
    >>>                                        filename="attachment.txt"))

    """

    _common.validate_argument_types([
        (to, 'to', (str, EmailRecipient, List)),
        (subject, 'subject', str),
        (content, 'content', str),
        (cc, 'cc', (str, EmailRecipient, List)),
        (bcc, 'bcc', (str, EmailRecipient, List)),
        (attachments, 'attachments', (EmailAttachment, List)),
        (errors, 'errors', str),
        (quiet, 'quiet', bool),
        (status, 'status', Status),
        (session, 'session', Session)
    ])

    status = Status.validate(status, quiet, errors)
    session = Session.validate(session)
    _login.validate_login(session, status)

    email_request_body: EmailRequestInput = _create_email_request_input(to, subject, content, cc, bcc, attachments)

    status.update('Sending...', Status.RUNNING)

    try:
        _call_send_email_api(session, email_request_body)
    except Exception as e:
        if status.errors == 'raise':
            raise e
        status.update(str(e), Status.FAILURE)
        return

    status.update('Your message has been sent', Status.SUCCESS)
