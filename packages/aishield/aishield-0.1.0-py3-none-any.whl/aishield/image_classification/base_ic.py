import os
from pprint import pprint

from aishield.constants import Task, SupportedFramework
from aishield.utils.util import get_class_attributes


class ICVulnerabilityConfig:
    """
    Instatiates the base class for vulnerability config of Image Classification

    Returns
    -------
    Initialized config parameters required for vulnerability analysis 
    """

    def __init__(self, defense_generate):
        """
        Initializes the vulnerability config parameters for Image Classification task
        Parameters
        ----------
        defense_generate: if defense needs to be generated if vulnerabilities found in the model
        """
        self.input_dimensions = None
        self.number_of_classes = None
        self.normalize_data = "yes"
        self.number_of_attack_queries = 200
        self.model_framework = "tensorflow"
        self.encryption_strategy = 0
        self.defense_bestonly = "no"
        self.use_model_api = 'no'
        self.model_api_details = ''
        if defense_generate:
            self.vulnerability_threshold = 0
        else:
            self.vulnerability_threshold = 1
        self.task_type = Task.IMAGE_CLASSIFICATION

    def get_all_params(self):
        """
        Get the initialized configs for vulnerability analysis
        Returns
        -------
        class_attribs: initialized configs
        """
        class_attribs = get_class_attributes(self)
        # pprint(class_attribs)
        return class_attribs

    @property
    def input_dimensions(self):
        return self.__input_dimensions

    @input_dimensions.setter
    def input_dimensions(self, input_dimensions):
        if input_dimensions:
            height, width, channel = input_dimensions[0], input_dimensions[1], input_dimensions[2]
            valid_channel_val = channel == 1 or channel == 3
            if not valid_channel_val:
                raise Exception('channel must be 1(greyscale) or 3(color)')
            input_dimensions = str(input_dimensions)
        self.__input_dimensions = input_dimensions

    @property
    def number_of_classes(self):
        return self.__number_of_classes

    @number_of_classes.setter
    def number_of_classes(self, num_classes):
        if num_classes and num_classes == 0:
            raise Exception('Number of classes must be >=1')
        self.__number_of_classes = num_classes

    @property
    def normalize_data(self):
        return self.__normalize_data

    @normalize_data.setter
    def normalize_data(self, normalize_data):
        self.__normalize_data = normalize_data

    @property
    def number_of_attack_queries(self):
        return self.__number_of_attack_queries

    @number_of_attack_queries.setter
    def number_of_attack_queries(self, num_attack_queries):
        self.__number_of_attack_queries = num_attack_queries

    @property
    def model_framework(self):
        return self.__model_framework

    @model_framework.setter
    def model_framework(self, model_framework):
        if model_framework.lower() not in SupportedFramework.valid_types():
            raise Exception('model_framework provided {} not supported. Supported: {}'
                            .format(model_framework, ', '.join(SupportedFramework.valid_types())))
        self.__model_framework = model_framework

    @property
    def encryption_strategy(self):
        return self.__encryption_strategy

    @encryption_strategy.setter
    def encryption_strategy(self, encryption_strategy):
        valid_encryption_strategy = [0, 1]
        if encryption_strategy not in valid_encryption_strategy:
            raise Exception('encryption_strategy can be 0 or 1')
        self.__encryption_strategy = encryption_strategy

    @property
    def defense_bestonly(self):
        return self.__defense_bestonly

    @defense_bestonly.setter
    def defense_bestonly(self, defense_bestonly):
        self.__defense_bestonly = defense_bestonly


class ICVulnerabilityAnalysis:
    """
    Instantiate for performing vulnerability analysis
    """
    def __init__(self, data_path: str, label_path: str, model_path: str, payload: dict):
        self.data_path = data_path
        self.label_path = label_path
        self.model_path = model_path
        self.payload = payload

    @property
    def data_path(self):
        return self.__data_path

    @data_path.setter
    def data_path(self, data_path):
        if not data_path:
            raise Exception('data_path must be provided for vulnerability analysis')
        self.__data_path = data_path

    @property
    def label_path(self):
        return self.__label_path

    @label_path.setter
    def label_path(self, label_path):
        if not label_path:
            raise Exception('label_path must be provided for vulnerability analysis')
        self.__label_path = label_path

    @property
    def model_path(self):
        return self.__model_path

    @model_path.setter
    def model_path(self, model_path):
        if not model_path:
            raise Exception('model_config details must be provided for vulnerability analysis')
        self.__model_path = model_path

    @property
    def payload(self):
        return self.__payload

    @payload.setter
    def payload(self, payload):
        if not payload:
            raise Exception('vuln_config details must be provided for vulnerability analysis')
        self.__payload = payload

    def prep_analysis_payload(self):
        """
        Prepares the payload required to perform the vulnerability analysis

        Returns
        -------
        files: having data, lebal and model file
        payload: configs of vulnerability analysis
        """
        data_name = os.path.split(self.data_path)[1]  # data file name
        label_name = os.path.split(self.label_path)[1]  # label file name
        model_name = os.path.split(self.model_path)[1]  # model file name
        files = [
            ('data_zip', (data_name, open(self.data_path, 'rb'), 'application/x-zip-compressed')),
            ('model_zip', (model_name, open(self.model_path, 'rb'), 'application/x-zip-compressed')),
            ('label_zip', (label_name, open(self.label_path, 'rb'), 'application/x-zip-compressed'))
        ]
        return files, self.payload
