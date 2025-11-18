import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

DATABASE_NAME = "db-covid"

TABLE_NAME = "covidrds_public_casos_municipios"

S3_OUTPUT_PATH = "s3://proyecto3datalake/raw/rds/"

# Leer datos
datasource = glueContext.create_dynamic_frame.from_catalog(
    database = DATABASE_NAME,
    table_name = TABLE_NAME,
    transformation_ctx = "datasource"
)

#Escribe datos
datasink = glueContext.write_dynamic_frame.from_options(
    frame = datasource,
    connection_type = "s3",
    connection_options = {"path": S3_OUTPUT_PATH},
    format = "parquet",
    format_options = {"compression": "snappy"},
    transformation_ctx = "datasink"
)


job.commit()