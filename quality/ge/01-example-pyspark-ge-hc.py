#
# File: https://github.com/data-engineering-helpers/data-contracts/blob/main/quality/ge/01-example-pyspark-ge-hc.py
#
# Inspired by
# https://towardsdatascience.com/data-contracts-the-mesh-glue-c1b533e2a664
# => https://gist.githubusercontent.com/velascoluis/268f73916f22fbaa070f9aba64c948f6/raw/71b85e11e0e7e81be7a665809ee1655e77669594/evaluate_ge_spark.py
# Original author: Luis Velasco
#
import pyspark
from pyspark.sql import SparkSession
import argparse
import json
import logging
from great_expectations.dataset import SparkDFDataset


def evaluate_contract(
    table_name: str = None,
    gcs_warehouse_dir: str = None,
    contract_config_str: str = None,
):
    """
    Evaluate a data contract using great expectations with pySPARK
    Parameters
    ----------
    table_name: The iceberg table where we will evaluate the contract against
    gcs_warehouse_dir: Iceberg GCS data location
    contract_config_str: JSON representation of the contract with the following format
        data_contract:
            version: 1
            environment: pro
            name: polyexpose
            table_schema:
                dq_slos:
                    mismatch_pct_lt: 0.2
                    nulls_pct_lt: 0.2
                    field_name: registration_dttm
                    nulls_allowed: true
                    required: true
                    type: TIMESTAMP
                    values_in: None

    Returns:
    --------
        None
    """
    config = pyspark.SparkConf().setAll(
        [
            (
                "spark.sql.extensions",
                "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions",
            ),
            (
                "spark.sql.catalog.spark_catalog",
                "org.apache.iceberg.spark.SparkSessionCatalog",
            ),
            ("spark.sql.catalog.spark_catalog.type", "hive"),
            ("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog"),
            ("spark.sql.catalog.local.type", "hadoop"),
            ("spark.sql.catalog.local.warehouse", gcs_warehouse_dir),
        ]
    )

    spark = SparkSession.builder.config(conf=config).getOrCreate()
    spark.sparkContext.setLogLevel("WARN")
    contract_config = json.loads(contract_config_str)
    logging.info("POLYEXPOSE - Reading table: " + table_name + "\n")
    df = spark.table(table_name)
    logging.info("POLYEXPOSE - Starting to validate contract \n ")
    df_ge = SparkDFDataset(df)
    logging.info("POLYEXPOSE -Schema required fields validation \n ")
    mandatory_columns = []
    for field in contract_config["data_contract"]["table_schema"]:
        if bool(field["required"]):
            mandatory_columns.append(field["field_name"])
    for column in mandatory_columns:
        try:
            assert df_ge.expect_column_to_exist(
                column
            ).success, f"POLYEXPOSE - Required {column} not found in table:FAILED"
            logging.info(f"POLYEXPOSE -{column} exists - PASSED \n ")
        except AssertionError as e:
            logging.error(e)
    spark.stop()
