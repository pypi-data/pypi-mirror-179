import os
from aishield.constants import (
    FileFormat,
    ReportType,
)


class JobDetails:
    """
    Instantiates to details of a vulnerability analysis job
    """
    def __init__(self, job_id=None, job_monitor_uri=None):
        """
        Constructor for Job Details class.
        Parameters
        ----------
        job_id: job_id of the submitted job
        job_monitor_uri: uri for monitoring the progress of job
        """
        self.job_id = job_id
        self.job_monitor_uri = job_monitor_uri

    @property
    def job_id(self):
        return self.__job_id

    @job_id.setter
    def job_id(self, job_id):
        self.__job_id = job_id

    @property
    def job_monitor_uri(self):
        return self.__job_monitor_uri

    @job_monitor_uri.setter
    def job_monitor_uri(self, job_monitor_uri):
        self.__job_monitor_uri = job_monitor_uri


class OutputConf:
    """
    OutputConf for getting reports(vulnerability/defense) or artifacts(defense model/sample attack data)
    """

    def __init__(self, report_type: ReportType = ReportType.VULNERABILITY, file_format: FileFormat = FileFormat.PDF,
                 save_folder_path=os.getcwd()):
        """
        Sets the OutputConf for getting reports(vulnerability/defense) or artifacts(defense model/sample attack data)
        Parameters
        ----------
        report_type: Report Type (Options : Vulnerability , Defense, Defense_artifact, Attack_samples)
        file_format: File format Type (Options : all, txt , pdf, json, xml}
        save_folder_path: output path where the artifacts would be saved
        """
        self.report_type = report_type
        self.file_format = file_format
        self.save_folder_path = save_folder_path

    @property
    def report_type(self):
        return self.__report_type

    @report_type.setter
    def report_type(self, report_type):
        self.__report_type = report_type

    @property
    def file_format(self):
        return self.__file_format

    @file_format.setter
    def file_format(self, file_format):
        self.__file_format = file_format

    @property
    def save_folder_path(self):
        return self.__save_folder_path

    @save_folder_path.setter
    def save_folder_path(self, save_folder_path):
        self.__save_folder_path = save_folder_path
