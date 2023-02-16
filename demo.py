from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation
from housing.util.util import read_yaml_file

def main():
    try:

        pipeline = Pipeline()
        pipeline.run_pipeline()
        #data_validation_config = Configuration().get_data_transformation_config()
        #print(data_validation_config)
        #schema_file_path = r"C:\Users\Praveen\machineLearningProject\config\schema.yaml"
        #file_path = r"C:\Users\Praveen\machineLearningProject\housing\artifact\data_ingestion\2023-01-30-09-27-22\ingested_data\train\housing.csv"
        #df = DataTransformation.load_data(file_path=file_path, schema_file_path=schema_file_path)
        #print(read_yaml_file(file_path=schema_file_path))
        #print(df.columns)
        #print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()