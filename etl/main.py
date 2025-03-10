from etl_cleaning import etl_cleaning_pipeling
from etl_splitting_dataset import etl_splitting_dataset_pipeline
from etl_training import etl_training_pipeline
from etl_predicting import etl_predicting_pipeline
from prefect import flow

def main():
    etl_cleaning_pipeling()
    etl_splitting_dataset_pipeline()
    etl_training_pipeline()
    etl_predicting_pipeline()

if __name__ == '__main__':
    main()