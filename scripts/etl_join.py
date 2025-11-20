import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

BUCKET_NAME = "proyecto3datalake2"
RAW_COVID_PATH = f"s3://{BUCKET_NAME}/raw/covid/url/casos_covid.csv.gz" 
RAW_MUNICIPIOS_PATH = f"s3://{BUCKET_NAME}/raw/rds/"
TRUSTED_OUTPUT_PATH = f"s3://{BUCKET_NAME}/trusted/enriquecido/"

spark = SparkSession.builder.appName("ETL_Join").getOrCreate()

df = spark \
    .read \
    .format("csv") \
    .option("compression", "gzip") \
    .option("header", True) \
    .load(RAW_COVID_PATH)

real_col = [c for c in df.columns if "DIVIPOLA" in c and "municipio" in c.lower()][0]

df = df.withColumnRenamed(real_col, "cod_divipola")

df_municipios = spark.read.parquet(RAW_MUNICIPIOS_PATH)


df_trusted = df.join(
    df_municipios,
    df["cod_divipola"] == df_municipios["codigo_divipola"],
    how="left"
).drop(
    df_municipios["codigo_divipola"]
)

df_trusted.write.mode("overwrite").parquet(
    TRUSTED_OUTPUT_PATH,
    compression="snappy"
)

