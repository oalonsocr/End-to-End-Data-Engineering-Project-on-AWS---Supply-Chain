import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)



# leer los datos de loading
df_raw = spark.read.option("header","True")\
                   .csv('s3://sc-analytics-lake-project/landing/supply_chain_data.csv')

# quitar espacio de encabezado
df_clean = df_raw.toDF(*(c.replace(' ', '_').lower() for c in df_raw.columns))


# transfromaciones

df_silver = (
    df_clean
    .withColumn("price",col("price").cast("float"))
    .withColumn("revenue_generated", col("revenue_generated").cast("float"))
    .withColumn("number_of_products_sold",col("number_of_products_sold").cast("int"))
    .withColumn("manufacturing_costs", col("manufacturing_costs").cast("float"))
    .withColumn(
        "stock_levels",
        when(col("stock_levels")< 0, 0)
        .otherwise(col("stock_levels")).cast("int")
    )
    .dropna(subset=["product_type"])
    .withColumn("ingestion_timestamp", current_timestamp())
    )


# Escritura parquet

df_silver.write \
    .mode("overwrite")\
    .format("parquet")\
    .partitionBy("product_type")\
    .save("s3://sc-analytics-lake-project/processed/supply_chain/")

job.commit()