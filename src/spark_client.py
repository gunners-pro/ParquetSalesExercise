from pyspark.sql import SparkSession

def get_spark() -> SparkSession:
    return (
        SparkSession.builder \
            .remote("sc://localhost:15002") \
            .appName("Parquet Sales") \
            .getOrCreate()
    )