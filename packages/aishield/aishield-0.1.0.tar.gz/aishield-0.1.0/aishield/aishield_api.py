from typing import Optional, List

from aishield.connection import RequestProcessor
from aishield.constants import (
    FileFormat,
    ReportType,
    Attack,
    Task
)
from aishield.configs import OutputConf
from aishield.image_classification import (
    extraction
)
from aishield.utils.util import (
    uri_validator,
    get_all_keys_by_val
)


class VulnConfig:
    """
    Instantiates the vulnerability configs based on task and attack type
    """

    def __new__(cls, task_type: Optional[Task] = Task.IMAGE_CLASSIFICATION,
                attack: Optional[Attack] = Attack.EXTRACTION,
                defense_generate: Optional[bool] = True):
        """
        Return the Vulnerability Config object

        Parameters
        ----------
        task_type: Type of task. Example: Image Classification, Image Segmentation, NLP, etc.
        attack: Type of attack for which vulnerability assessment has to be done.Example: Extraction, evasion, etc.
        defense_generate: Boolean flag to specify if defense needs to be generated if model found to be vulnerable

        Returns
        -------
        vul_config_obj : Class Object
        """
        task_type_val = task_type.value
        attack_val = attack.value
        if task_type_val not in Task.valid_types():
            raise ValueError('task_type param value {} is not in one of the accepted values {}.'.format(task_type_val,
                                                                                                        Task.valid_types()))
        if attack_val not in Attack.valid_types():
            raise ValueError('attack param value {} is not in one of the accepted values {}.'.format(attack_val,
                                                                                                     Attack.valid_types()))

        if task_type == Task.IMAGE_CLASSIFICATION:
            if attack == Attack.EXTRACTION:
                vul_config_obj = extraction.VulnConfig(defense_generate)
            elif attack == Attack.EVASION:
                raise NotImplementedError('Feature coming soon')
            else:
                raise NotImplementedError('Feature coming soon')
        elif task_type == 'tsf':
            raise NotImplementedError('Feature coming soon')
        elif task_type == 'nlp':
            raise NotImplementedError('Feature coming soon')
        elif task_type == 'image_segmentation':
            raise NotImplementedError('Feature coming soon')
        else:
            raise NotImplementedError('New task-pairs would be added soon')
        return vul_config_obj


class AIShieldApi:
    """
    Instantiates for performing vulnerability analysis
    """

    def __init__(self, api_url: str, auth_token: str):
        """
        Initializes the AIShield API with request headers

        Parameters
        ----------
        api_url: api endpoint of AIShield vulnerability analysis
        auth_token: user subscription key
        """
        if not api_url:
            raise ValueError('aishield api is not provided')
        if not auth_token:
            raise ValueError('auth_token is not provided')
        if not uri_validator(api_url):
            raise ValueError('aishield api is invalid')

        headers = {
            'Cache-Control': 'no-cache',
            'Ocp-Apim-Subscription-Key': auth_token
        }
        self.request_processor = RequestProcessor(api_url, headers)

    def vuln_analysis(self, data_path: str = None, label_path: Optional[str] = None,
                      model_path: Optional[str] = None, reference_models: Optional[List[str]] = None,
                      vuln_config: Optional[VulnConfig] = None):
        """
        Perform Vulnerability analysis of the model

        Parameters
        ----------
        data_path: path of zipped data folder
        label_path: path of zipped label folder.
        model_path: model path to zipped model file(s) either in encrypted or unencrypted format or model API details of ModelConf type
        reference_models: list of reference models.
        vuln_config: configs for vulnerability analysis of VulnConfig type

        Returns
        -------
        status: job status: success or failed
        job_details: having information such as job_id, monitoring link
        """

        payload = {key: getattr(vuln_config, key) for key in dir(vuln_config) if not key.startswith('_')}
        # validation - raise error any key in payload has None value
        keys_with_none_val = get_all_keys_by_val(payload, None)
        if keys_with_none_val:
            raise ValueError('None values found for {}.'.format(', '.join(keys_with_none_val)))

        task_type = vuln_config.task_type
        attack_strategy = vuln_config.attack

        if task_type == Task.IMAGE_CLASSIFICATION:
            if attack_strategy == Attack.EXTRACTION:
                va_extraction = extraction.VulnAnalysis(data_path, label_path, model_path, payload)
                files, payload = va_extraction.prep_analysis_payload()
                # part_uri = PartURI.IMAGE_CLASSIFICATION.value
            else:
                raise NotImplementedError('Feature coming soon')
        elif task_type == Task.TIMESERIES_FORECAST:
            raise NotImplementedError('Feature coming soon')

        elif task_type == Task.NLP:
            raise NotImplementedError('Feature coming soon')

        elif task_type == Task.IMAGE_SEGMENTATION:
            raise NotImplementedError('Feature coming soon')

        else:
            raise NotImplementedError('New task-pairs would be added soon')

        # Update payload
        del payload['task_type']
        del payload['attack']
        # Update URL based on the type of task selected
        # self.request_processor.api_endpoint = self.request_processor.api_endpoint + '/' + part_uri

        status, job_details = self.request_processor.send(files=files, payload=payload)
        return status, job_details

    def job_status(self, job_id):
        """
        Prints the status of each vulnerability analysis while the job is running.
        Once job completes, returns with status: success or failed

        Parameters
        ----------
        job_id: job_id returned from the request

        Returns
        -------
        status: success or failed
        """
        status = self.request_processor.get_job_status(job_id=job_id)
        return status

    def save_job_report(self, job_id: str = None, output_config: OutputConf = None) -> str:
        """
        Save the artifacts of the vulnerability analysis.

        Parameters
        ----------
        job_id: job_id returned from the request
        output_config: object with OutputConf Type

        Returns
        -------
        saved_loc: location where the artifact got saved.
        """
        if not job_id or job_id is None:
            raise ValueError('invalid job id value')
        file_format = output_config.file_format.value.lower()
        report_type = output_config.report_type.value.lower()
        save_folder_path = output_config.save_folder_path

        if file_format not in FileFormat.valid_types():
            raise ValueError('invalid file_format value {}. Must be one of {}'.format(file_format,
                                                                                      FileFormat.valid_types()))
        if report_type not in ReportType.valid_types():
            ValueError('invalid report_type value {}. Must be one of {}'.format(report_type,
                                                                                ReportType.valid_types()))
        saved_loc = self.request_processor.get_artifacts(job_id=job_id, report_type=report_type,
                                                         file_format=file_format,
                                                         save_folder_path=save_folder_path)
        return saved_loc
