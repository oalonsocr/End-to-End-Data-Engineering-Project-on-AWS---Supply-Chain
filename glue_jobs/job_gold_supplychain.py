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


# Leer la capa silver
df_silver = spark.read.parquet("s3://sc-analytics-lake-project/processed/supply_chain/")


# creando kpi de negocio
df_gold = (
    df_silver
    .withColumn(
        "manufacturing_efficiency",
        (col("revenue_generated") - col("manufacturing_costs"))/ col("number_of_products_sold")
    )
    .withColumn(
        "lead_time_status",
        when(col("lead_time")> 15, "Delayed")
        .otherwise("on-time")
    )
)


# creando tabla de echos

df_fact = df_gold.select(
    "product_type",
    "number_of_products_sold",
    "revenue_generated",
    "manufacturing_costs",
    "manufacturing_efficiency",
    "lead_time_status"
)


# Guardando en gold y registrando catalog
spark.sql("CREATE DATABASE IF NOT EXISTS db_supply_chain")

df_fact.write\
       .mode("overwrite")\
       .format("parquet")\
       .option("path","s3://sc-analytics-lake-project/gold/fact_supply_chain")\
       .saveAsTable("db_supply_chain.fact_supply_chain")


job.commit()