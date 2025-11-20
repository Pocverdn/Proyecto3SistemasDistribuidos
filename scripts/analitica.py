import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count, lit, round, when, avg

BUCKET_NAME = "proyecto3datalake2"
TRUSTED_INPUT_PATH = f"s3a://{BUCKET_NAME}/trusted/enriquecido/"
REFINED_OUTPUT_PATH = f"s3a://{BUCKET_NAME}/refined/analisis/"

spark = SparkSession.builder.appName("ETL_Analitica").getOrCreate()

df_trusted = spark.read.parquet(TRUSTED_INPUT_PATH)

df_analisis = df_trusted.groupBy("nombre departamento", "poblacion").agg(
    count(lit(1)).alias("casos_totales"),
        
    sum(when(col("Recuperado") == "Fallecido", 1).otherwise(0)).alias("fallecidos_totales"),
    sum(when(col("Recuperado") == "Recuperado", 1).otherwise(0)).alias("recuperados_totales"),
    avg("camas_uci_disponibles").alias("promedio_camas_uci")
)

df_analisis = df_analisis.withColumn(
    "tasa_letalidad_pct",
    round((col("fallecidos_totales") / col("casos_totales")) * 100, 2)
)

df_analisis = df_analisis.withColumn(
    "casos_por_100k_hab",
    round((col("casos_totales") / col("poblacion")) * 100000, 2)
)

df_analisis.createOrReplaceTempView("vista_analisis_departamental")

df_refined_output = spark.sql("""
    SELECT 
        `nombre departamento`,
        casos_totales,
        fallecidos_totales,
        tasa_letalidad_pct,
        casos_por_100k_hab,
        promedio_camas_uci
    FROM 
        vista_analisis_departamental
    WHERE 
        `nombre departamento` IS NOT NULL
    ORDER BY 
        casos_por_100k_hab DESC
    LIMIT 10
""")

df_refined_output.coalesce(1).write.mode("overwrite").parquet(
    REFINED_OUTPUT_PATH,
    compression="snappy"
)
spark.stop()
