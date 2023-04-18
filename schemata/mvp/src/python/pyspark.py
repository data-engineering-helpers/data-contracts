#
# File: https://github.com/data-engineering-helpers/data-contracts/tree/main/schemata/mvp/src/python/pyspark.py
#

from pyspark.sql import SparkSession

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
    .options(delimiter="^", header=True, inferSchema=True)
    .csv(routeFile)
    .cache()
    )

#
routeData.show()

#
spark.stop()

