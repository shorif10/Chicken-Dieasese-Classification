from cnnClassifier.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipelines.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier import logger

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>stage {STAGE_NAME} started<<<")
    data_ingestion  = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>stage {STAGE_NAME} completed<<<")
except Exception as e:
    logger.error(f">>>stage {STAGE_NAME} failed<<<")
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f'************************')
    logger.info(f">>>>>>stage {STAGE_NAME} started <<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)
    raise e