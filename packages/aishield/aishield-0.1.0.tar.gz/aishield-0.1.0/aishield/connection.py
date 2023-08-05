import json
import os
import time
from datetime import datetime
import requests

from aishield.configs import JobDetails
from aishield.utils.exceptions import AIShieldException
from aishield.utils import logger

LOG = logger.getLogger(__name__)


class RequestProcessor:
    def __init__(self, api_endpoint, headers):
        """
        Initialize with the api endpoint and headers required for calling to AIShield API
        Parameters
        ----------
        api_endpoint: api endpoint of AIShield vulnerability analysis
        headers: headers for the request
        """
        self.api_endpoint = api_endpoint
        self.headers = headers

    def send(self, files, payload):
        """
        Sends HTTP Post request to api_endpoint.
        Parameters
        ----------
        files: needed for analysis
        payload: dictionary, which is sent as as JSON.

        Returns
        -------
        the status of job with details
        raises AIShieldException in case of errors or if the response from server does not indicate 'SUCCESS'.
        """
        status = 'failed'
        job_details = JobDetails()
        job_send_url = self.api_endpoint
        # job_send_url = self.api_endpoint + '/VulnerabiltyReport'
        try:
            response = requests.post(url=job_send_url, params=payload, files=files, headers=self.headers)
            response.raise_for_status()
        except requests.RequestException as e:
            raise AIShieldException(e)

        resp_json = None

        try:
            resp_json = response.json()
        except ValueError:
            raise AIShieldException(
                'Error response from server: {}{}'.format(
                    response.text[0:150], len(response.text) > 150 and '...' or ''
                )
            )
        if 'job_id' in resp_json:
            status = 'success'
            job_details.job_id = resp_json['job_id']
            job_details.job_monitor_uri = resp_json['monitor_link']

        return status, job_details

    def get_job_status(self, job_id) -> str:
        """
        Monitor progress for job id

        Parameters
        ----------
        job_id: id of the submitted job

        Returns
        -------
        Logs the status of individual steps of analysis and returns the final status of the task
        """
        job_status_url = self.api_endpoint[:-18] + "JobStatusDetailed?JobID=" + job_id
        status_dictionary = {
            'ModelExploration_Status': 'na',
            'SanityCheck_Status': 'na',
            'QueryGenerator_Status': 'na',
            'VunerabilityEngine_Status': 'na',
            'DefenseReport_Status': 'na',
        }
        LOG.info('Fetching job details for job id {}'.format(job_id))
        while (True):
            time.sleep(5)
            try:
                job_status_response = requests.request("GET", job_status_url, headers=self.headers, timeout=15)
                job_status_payload = json.loads(job_status_response.text)
            except requests.RequestException as e:
                raise AIShieldException(e)

            final_status = 'failed'
            failing_key = ''
            for key in status_dictionary.keys():
                if status_dictionary[key] == 'na':
                    if job_status_payload[key] == 'completed' or job_status_payload[key] == 'passed':
                        status_dictionary[key] = job_status_payload[key]
                        LOG.info(str(key) + ":" + status_dictionary[key])
                        print('running...', end='\r')
                    elif job_status_payload[key] == 'failed':
                        failing_key = key
                        status_dictionary[key] = job_status_payload[key]
                        LOG.info(str(key) + ":" + status_dictionary[key])
                        print('running...', end='\r')

            if failing_key and status_dictionary[failing_key] == 'failed':
                break

            if status_dictionary['VunerabilityEngine_Status'] == 'passed' or status_dictionary[
                'VunerabilityEngine_Status'] == 'completed' and job_status_payload[
                'CurrentStatus'] == "Defense generation is not triggered":
                LOG.info("\n Vulnerability score {} failed to cross vulnerability threshold of {}".format(
                    job_status_payload['VulnerabiltyScore']))
                final_status = 'success'
                break
            if job_status_payload['DefenseReport_Status'] == 'completed':
                final_status = 'success'
                break
        LOG.info('job run completed')
        return final_status

    def get_artifacts(self, job_id, report_type, file_format, save_folder_path) -> str:
        """
        Get the artifacts like reports, attack samples or defense model

        Parameters
        ----------
        job_id: id of the submitted job
        report_type: type of report/artifact to be fetched
        file_format: format in which the file to be saved
        save_folder_path: folder path where the artifact will be saved

        Returns
        -------
        file_path: path of saved report/artifact
        """
        if report_type.lower() in ['vulnerability', 'defense']:
            if file_format == 'txt':
                file_format_id = 1
            elif file_format == 'pdf':
                file_format_id = 2
            elif file_format == 'json':
                file_format_id = 3
            elif file_format == 'xml':
                file_format_id = 4
            else:
                file_format_id = 0
                file_format = 'zip'  # all reports zipped
        if report_type.lower() in ['defense_artifact', 'attack_samples']:
            file_format_id = 0
            file_format = 'zip'

        job_artifact_url = self.api_endpoint[:-18] + "GetReport?JobID=" + job_id + \
                           "&ReportType={}&FileFormat={}".format(report_type, file_format_id)
        # job_artifact_url = self.api_endpoint + "/GetReport?JobID=" + job_id + \
        #                    "&ReportType={}&FileFormat={}".format(report_type, file_format_id)
        job_status_response = requests.request("GET", job_artifact_url, params={}, headers=self.headers)
        time_now = datetime.now().strftime("%Y%m%d_%H%M")
        file_name = '{}_{}.{}'.format(report_type, time_now, file_format)
        file_path = os.path.join(save_folder_path, file_name)
        with open(file_path, "wb") as f:
            f.write(job_status_response.content)
        LOG.info('{} is saved in {}'.format(file_name, save_folder_path))
        return file_path
