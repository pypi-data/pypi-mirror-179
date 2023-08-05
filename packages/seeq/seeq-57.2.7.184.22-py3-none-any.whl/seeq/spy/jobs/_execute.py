from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import Union

import nbconvert
import nbformat
from nbformat import NotebookNode

from seeq.spy import _datalab
from seeq.spy._errors import *

RESULTS_FOLDER = '_Job Results/'
CELL_EXECUTION_TIMEOUT = 86400


class ExecutionInstance:
    _logger = None

    def __init__(self):
        if not _datalab.is_executor():
            raise SPyRuntimeError('Execution of notebooks is not supported through SPy interface.')

        self.file_path = os.environ.get('SEEQ_SDL_FILE_PATH', '')
        self.label = os.environ.get('SEEQ_SDL_LABEL', '')
        self.index = os.environ.get('SEEQ_SDL_SCHEDULE_INDEX', '')
        self.job_key = os.environ.get('SEEQ_SDL_JOB_KEY', '')
        scheduled_file_filename: str = Path(self.file_path).name
        scheduled_file_folder: Path = Path(self.file_path).parent
        # merged_notebook_path is our new scheduled notebook with login cell
        self.merged_notebook_path = _compose_filename(self.index, self.label,
                                                      scheduled_file_filename,
                                                      scheduled_file_folder,
                                                      extension='.ipynb', result=False)
        # This is our resulting html file after execution
        self.job_result_path = _compose_filename(self.index, self.label,
                                                 scheduled_file_filename,
                                                 scheduled_file_folder,
                                                 extension='.html', result=True)

    @property
    def logger(self) -> logging.Logger:
        """
        Logger to be used for logging inside executor container
        """
        if self._logger is not None:
            return self._logger

        log_level = get_log_level_from_executor()

        # python logging doesnt have TRACE
        log_level = "DEBUG" if log_level == "TRACE" else log_level

        executor_logger = logging.getLogger("executor_logger")
        exec_handler = logging.StreamHandler(sys.stdout)
        exec_formatter = logging.Formatter(
            f'%(levelname)s - Notebook {self.file_path.replace("%", "%%")} with jobKey {self.job_key} %(message)s')
        exec_handler.setFormatter(exec_formatter)
        executor_logger.addHandler(exec_handler)
        executor_logger.setLevel(log_level)

        self._logger = executor_logger
        return executor_logger

    def execute(self):
        # Abort if scheduled notebook does not exist
        if not Path(self.file_path).exists():
            # TODO CRAB-25884: unschedule the notebook if no longer exists and notify the creator
            self.logger.error('not found, aborting')
            return

        # noinspection PyBroadException
        try:
            # Create the new scheduled notebook with login cell
            self.create_merged_notebook()

            # Execute the new scheduled notebook with login cell
            self.execute_merged_notebook()

            # Convert to html and save
            self.export_html()

            # Log success for executor
            self.logger.info('succeeded')
        except BaseException as e:
            self.logger.error('encountered error', exc_info=e)
        finally:
            # Cleanup
            if Path(self.merged_notebook_path).exists():
                Path(self.merged_notebook_path).unlink()

    def create_merged_notebook(self):
        # Open the notebook that has been scheduled for execution
        with open(self.file_path) as f_notebook_scheduled:
            nb_notebook_scheduled = nbformat.read(f_notebook_scheduled, nbformat.NO_CONVERT)

        # Get kernel language
        language = _datalab.get_notebook_language(nb_notebook_scheduled)
        if not language:
            error_message = f'could not determine language for {f_notebook_scheduled}'
            self.logger.error(error_message)
            raise SPyRuntimeError(error_message)

        # Get execution notebook
        execution_notebook = _datalab.get_execution_notebook(language)
        if not execution_notebook:
            error_message = f'could not find execution notebook for {f_notebook_scheduled} with language {language}'
            self.logger.error(error_message)
            raise SPyRuntimeError(error_message)

        # Open the dummy notebook with spy.login cell
        with open(execution_notebook) as f_notebook_execution:
            nb_notebook_execution = nbformat.read(f_notebook_execution, nbformat.NO_CONVERT)

        # Create new notebook dynamically that includes login cell first
        nb_notebook_merged = NotebookNode(nb_notebook_execution.copy())

        # Add in cells from scheduled notebook
        nb_notebook_merged['cells'].extend(nb_notebook_scheduled.cells.copy())

        # Write out the new joined notebook as hidden notebook with the same name as scheduled notebook
        with open(self.merged_notebook_path, 'w') as f_notebook_merged:
            nbformat.write(nb_notebook_merged, f_notebook_merged)

        # Log to executor
        self.logger.debug('successfully merged execution notebook with scheduled notebook')

    def execute_merged_notebook(self) -> NotebookNode:
        # Open the notebook for execution
        with open(self.merged_notebook_path, 'r+') as f_notebook_merged:
            nb_notebook_merged = nbformat.read(f_notebook_merged, nbformat.NO_CONVERT)

        # Configure the execute processor to allow errors and the output path
        proc = nbconvert.preprocessors.ExecutePreprocessor(timeout=CELL_EXECUTION_TIMEOUT,
                                                           allow_errors=True)
        proc.preprocess(nb_notebook_merged, {'metadata': {'path': Path(self.file_path).parent}})

        # Log to executor
        self.logger.debug('successfully executed merged notebook')

        # Python logger has no TRACE level. Special logging case here since dumping notebook
        # contents can clog the log
        if is_log_level_trace_from_executor():
            self.logger.debug(f'executed notebook contents from {self.merged_notebook_path}:{nb_notebook_merged}')

        # Remove login cell from notebook
        del nb_notebook_merged['cells'][0]

        # Decrement the "execution_count" by 1 to correct notebook cell numbering
        # "execution_count" can have 'None' as value so just pass on any exception to continue
        for cell in nb_notebook_merged['cells']:
            # noinspection PyBroadException
            try:
                if 'execution_count' in cell:
                    execution_count = int(cell['execution_count'])
                    execution_count -= 1
                    cell['execution_count'] = execution_count
            except BaseException:
                pass

            if 'outputs' in cell:
                for output in cell['outputs']:
                    # noinspection PyBroadException
                    try:
                        if 'execution_count' in output:
                            execution_count = int(output['execution_count'])
                            execution_count -= 1
                            output['execution_count'] = execution_count
                    except BaseException:
                        pass

        # Write the scheduled notebook
        with open(self.merged_notebook_path, 'w') as f_notebook_merged:
            nbformat.write(nb_notebook_merged, f_notebook_merged)

        # Log to executor
        self.logger.debug('successfully edited merged notebook')

        # The executed notebook will be returned if spy.jobs.execute was called by a user
        return nb_notebook_merged

    def export_html(self):
        # Open the modified notebook that has been scheduled for execution
        with open(self.merged_notebook_path) as f_notebook_merged:
            nb_notebook_merged = nbformat.read(f_notebook_merged, nbformat.NO_CONVERT)

        # Configure the HTML exporter and export
        html_exporter = nbconvert.HTMLExporter()
        job_result_html, _ = html_exporter.from_notebook_node(nb_notebook_merged)

        # Create parent folder if not existing and write out the exported html to file
        Path(self.job_result_path).parent.mkdir(parents=True, exist_ok=True)
        with open(self.job_result_path, 'w') as f_job_result_file:
            f_job_result_file.write(job_result_html)

        # Log to executor
        self.logger.debug('successfully exported merged notebook')


def execute():
    """
    Execute a notebook. (Internal Seeq function: Not intended for end-users)
    """
    return ExecutionInstance().execute()


def _compose_filename(index, label, scheduled_file_filename, scheduled_file_folder, extension='.html', result=True):
    folder_path: Union[str, Path] = Path(scheduled_file_folder, RESULTS_FOLDER) if result else \
        scheduled_file_folder
    hidden_file_prefix = '.' if not result else ''
    filename_no_ext: str = hidden_file_prefix + Path(scheduled_file_filename).stem

    # Build up the job result html file name
    folder = str(folder_path)
    executor = ".executor"
    index = '.' + index if len(index) > 0 else ''
    label = '.' + label if len(label) > 0 else ''

    result_filename = f'{folder}/{filename_no_ext}{executor}{index}{label}{extension}'
    return result_filename


def get_log_level_from_executor():
    return str(os.environ.get('LOG_LEVEL', 'INFO')).upper()


def is_log_level_trace_from_executor():
    return get_log_level_from_executor() == "TRACE"
