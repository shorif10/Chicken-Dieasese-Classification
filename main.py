from cnnClassifier.pipelines.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier import logger

STAGE_NAME = 'Data Ingestion Stage'
if __name__ == '__main__':
    try:
        logger.info(f">>>stage {STAGE_NAME} started<<<")
        obj = DataIngestionPipeline()
        obj.main()
        logger.info(f">>>stage {STAGE_NAME} completed<<<")
    except Exception as e:
        logger.error(f">>>stage {STAGE_NAME} failed<<<")
        logger.exception(e)
        raise e