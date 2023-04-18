#
# File: https://github.com/data-engineering-helpers/data-contracts/tree/main/schemata/mvp/src/python/pyspark.py
#

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Schema
schema = StructType(
    [StructField("airline_id", StringType(), True),
     StructField("org_por", StringType(), True),
     StructField("dst_por", StringType(), True),
     StructField("freq", IntegerType(), True)]
)

# Data set - source: OpenTravelData (OPTD)
routeFile = "../../data/optd/optd_airline_por.csv"

# Initializes the Spark session
spark = (
    SparkSession
    .builder
    .appName("SchemataMVP")
    .getOrCreate()
    )

# Parse the data file
routeData = (
    spark
    .read
    .options(delimiter="^", header=True, schema=schema)
    .csv(routeFile)
    .cache()
    )

#
routeData.show()

#
spark.stop()

