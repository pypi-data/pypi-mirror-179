from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def valid_types(cls):
        return list(map(lambda c: c.value, cls))


class Attack(ExtendedEnum):
    EXTRACTION = 'extraction'
    EVASION = 'evasion'
    INFERENCE = 'inference'
    POISON = 'poison'


class Task(ExtendedEnum):
    IMAGE_CLASSIFICATION = 'image_classification'
    IMAGE_SEGMENTATION = 'image_segmentation'
    TIMESERIES_FORECAST = 'timeseries_forecast'
    NLP = 'nlp'


class ReportType(ExtendedEnum):
    VULNERABILITY = 'vulnerability'
    DEFENSE = 'defense'
    DEFENSE_ARTIFACT = 'defense_artifact'
    ATTACK_SAMPLES = 'attack_samples'


class FileFormat(ExtendedEnum):
    TXT = 'txt'
    PDF = 'pdf'
    JSON = 'json'
    XML = 'xml'
    ALL = 'all'


class SupportedFramework(ExtendedEnum):
    TENSORFLOW = 'tensorflow'


class PartURI(ExtendedEnum):
    IMAGE_CLASSIFICATION = 'ic/ais/ImageClassification'
    IMAGE_SEGMENTATION = 'is/ais/IMAGESEGMENTATION'
    TIMESERIES_FORECAST = 'tsf/ais/TIMESERIESFORECAST'
    NLP = 'nlp/ais/NLP'
