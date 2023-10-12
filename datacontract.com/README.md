Data Contracts - Datacontract.com
=================================

# Table of Contents (ToC)
* [Data Contracts - Datacontract.com](#data-contracts---datacontractcom)
* [Overview](#overview)
* [References](#references)
   * [DuckDB](#duckdb)
   * [Soda Core](#soda-core)
   * [OpenTravelData (OPTD)](#opentraveldata-optd)
* [Quickstart](#quickstart)
   * [Setup](#setup)
   * [Create a data contract](#create-a-data-contract)
   * [Import a data contract](#import-a-data-contract)
   * [Check the compliance of a data contract](#check-the-compliance-of-a-data-contract)
   * [Edit a data contract in Data Contract Studio](#edit-a-data-contract-in-data-contract-studio)
   * [Check the data quality of a table thanks to a data contract](#check-the-data-quality-of-a-table-thanks-to-a-data-contract)
* [Installation](#installation)
   * [On MacOS](#on-macos)
   * [On Linux](#on-linux)
   * [General](#general)
   * [Options](#options)
      * [DuckDB](#duckdb-1)
      * [Soda Core](#soda-core-1)
* [Trouble shooting](#trouble-shooting)
   * [Soda Core](#soda-core-2)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

# Overview
[This page](https://github.com/data-engineering-helpers/data-contracts/blob/main/datacontract.com/README.md)
is a deep dive on the [datacontract.com](https://datacontract.com/) ecosystem,
which includes an
[open specification](https://datacontract.com/) and
[some utilities](https://cli.datacontract.com/).

It is part of the larger
[Data contracts initiative](https://github.com/data-engineering-helpers/data-contracts).

# References
* Data Contract Specification: https://datacontract.com/
* Data contract command-line (CLI) utility:
  https://cli.datacontract.com/ (GitHub: https://github.com/datacontract/cli)
* Data Contract Studio: https://studio.datacontract.com/

## DuckDB
* [Data Engineering Helpers - Knowledge Sharing - DuckDB](https://github.com/data-engineering-helpers/ks-cheat-sheets/blob/main/db/duckdb/README.md)

## Soda Core
* Soda Core GitHub repository: https://github.com/sodadata/soda-core
* [Installation of Soda Core](https://github.com/sodadata/soda-core/blob/main/docs/installation.md)
  + [Configure Soda Core](https://github.com/sodadata/soda-core/blob/main/docs/configuration.md)
  + [Connect Soda to DuckDB](https://docs.soda.io/soda/connect-duckdb.html)

## OpenTravelData (OPTD)
* OpenTravelData GitHub repository with latest CSV snapshots:
  https://github.com/opentraveldata/opentraveldata/tree/master/opentraveldata/
* For instance, the sample file used here is about transportation routes:
  https://github.com/opentraveldata/opentraveldata/blob/master/opentraveldata/optd_airline_por.csv
  - A copy of that CSV file is also available on a public S3 bucket:
    [`s3://optd/latest/`](https://s3.console.aws.amazon.com/s3/buckets/optd?region=eu-west-1&tab=objects)

# Quickstart

## Setup
* If not already done so, clone this Git repository and change directory to it:
```bash
$ mkdir -p ~/dev/infra/data-contracts && \
  git clone https://github.com/data-engineering-helpers/data-contracts.git ~/dev/infra/data-contracts/data-contracts && \
  cd ~/dev/infra/data-contracts/data-contracts/datacontract.com
```

## Create a data contract
* Generate a new data contract, which will be a collection of
  commented samples (which may be then be uncommented following specific
  implementation details):
```bash
$ datacontract init --file contracts/orders-latest-npii-new.yaml
📄 data contract written to contracts/orders-latest-npii-new.yaml
```

## Import a data contract
* Import a data contract from a URL, creating a local replication of it
  + From Data Contract Studio:
```bash
$ datacontract init --from https://studio.datacontract.com/s/c8b27fe3-62dc-4a21-ae41-9471ce7859d7.yaml
📄 data contract written to datacontract.yaml
```
  + From some code repository, _e.g._, Git repositories (note that the URL
    to the raw YAML file should be retrieved here, otherwise, the retrieved
	file is HTML, not YAML):
```bash
$ datacontract init --overwrite-file --file data-contract-flight-route.yaml --from https://github.com/data-engineering-helpers/data-contracts/raw/main/datacontract.com/contracts/data-contract-flight-route.yaml
📄 data contract written to data-contract-flight-route.yaml
```

## Check the compliance of a data contract
* Check the validity of the data contract:
```bash
$ datacontract lint --file contracts/data-contract-flight-route.yaml
🟢 data contract is valid!
```

>**Note**
The schema specification of the
[`contracts/data-contract-flight-route-quality.yaml` data contract](https://github.com/data-engineering-helpers/data-contracts/tree/main/datacontract.com/contracts/data-contract-flight-route-quality.yaml)
is in its own YAML file, namely
[`contracts/data-contract-flight-route-schema.yaml`](https://github.com/data-engineering-helpers/data-contracts/tree/main/datacontract.com/contracts/data-contract-flight-route-schema.yaml),
cross-referenced by the data contract in the `schema` section.
That allows to use that schema specification with other tools, such as DBT
or Spark.

## Edit a data contract in Data Contract Studio
* Open the data contract in Data Contract Studio:
```bash
$ datacontract open --file contracts/data-contract-flight-route.yaml
🌐 opening data contract at https://studio.datacontract.com/s/16ff8cbb-7f3f-4ca4-addf-b3a4cbac1500
```

* Which results, for the
  [`contracts/data-contract-flight-route.yaml` data contract](https://github.com/data-engineering-helpers/data-contracts/tree/main/datacontract.com/contracts/data-contract-flight-route.yaml),
  into
  https://studio.datacontract.com/s/16ff8cbb-7f3f-4ca4-addf-b3a4cbac1500

* The data contract may be edited in the Data Contract Studio directly:
  https://studio.datacontract.com/s/16ff8cbb-7f3f-4ca4-addf-b3a4cbac1500/edit

## Check the data quality of a table thanks to a data contract
* The data quality check/test is not fully implemented yet. A feature request
  has been created for that purpose:
  https://github.com/datacontract/cli/issues/2
  
>**Note**
The data quality check section is located in its own YAML file, namely
[`contracts/data-contract-flight-route-quality.yaml`](https://github.com/data-engineering-helpers/data-contracts/tree/main/datacontract.com/contracts/data-contract-flight-route-quality.yaml),
cross-referenced by the data contract in the `quality` section.
That allows to use that data quality specification with other tools,
such as Soda or Great Expectations. Below is an example of use with Soda.
Note that this feature (of checking the data quality with external tools)
should be integrated in the `datacontract` CLI at
[some point in the future](https://github.com/datacontract/cli/issues/2).

* Launch a few data quality checks with Soda Core, with newer versions of the
  `datacontract` CLI, which wraps the SodaCL CLI
  + Setup Soda configuration within the `datacontract` CLI:
```bash
$ datacontract quality-init --file contracts/data-contract-flight-route.yaml --quality-file contracts/data-contract-flight-route-quality.yaml 
Creating quality directory if needed...
quality/
quality/soda-conf.yml 2023-10-12 17:54 86B
```

  + Create or copy the (`db.duckdb`) DuckDB database file (see the
    [DuckDB sub-section](#duckdb) below in order to initialize that DuckDB
    database file)
```bash
$ cp db.duckdb quality/
```

  + Launch the quality checks with the `datacontract` CLI:
```bash
$ datacontract quality-check --file contracts/data-contract-flight-route.yaml --quality-file contracts/data-contract-flight-route-quality.yaml 
[...]
[18:01:15] Soda Core 3.0.51
[18:01:16] Scan summary:
[18:01:16] 2/2 checks PASSED: 
[18:01:16]     transport_routes in duckdb_local
[18:01:16]       row_count between 90000 and 100000 [PASSED]
[18:01:16]       invalid_percent(freq) = 0 % [PASSED]
[18:01:16] All is good. No failures. No warnings. No errors.
```

* Launch a few data quality checks with Soda Core, directly with the SodaCL CLI
  (without the `datacontract` CLI):
```bash
$ soda scan -d duckdb_local -c soda-conf.yml contracts/data-contract-flight-route-quality.yaml
[16:16:10] Soda Core 3.0.50
[16:16:11] Scan summary:
[16:16:11] 2/2 checks PASSED: 
[16:16:11]     transport_routes in duckdb_local
[16:16:11]       row_count between 90000 and 100000 [PASSED]
[16:16:11]       invalid_percent(freq) = 0 % [PASSED]
[16:16:11] All is good. No failures. No warnings. No errors.
```

# Installation
* Install the `datacontract` CLI (command-line) utility

## On MacOS
* With HomeBrew
```bash
$ brew install datacontract/brew/datacontract
```

## On Linux
* Specify the platform and architecture of the machine:
```bash
export platform="$(uname | tr '[:upper:]' '[:lower:]')"
export architecture="$(uname -m|sed 's/x86_/amd/')"
```

* From the [GitHub releases](https://github.com/datacontract/cli/releases)
  + Specify the latest version:
```bash
$ DC_VERSION="0.1.1"
  DC_FN="datacontract-v$DC_VERSION-$platform-$architecture.tar.gz"
```
  + Download the CLI utility:
```bash
$ mkdir -p /tmp/datacontract
  pushd /tmp/datacontract
  curl -kL https://github.com/datacontract/cli/releases/download/v$DC_VERSION/$DC_FN -o $DC_FN
```
  + Install the CLI utility:
```bash
$ mkdir -p ~/.local/bin
  tar zxf $DC_FN && rm -f $DC_FN
  mv datacontract ~/.local/bin/ && rm -f LICENSE README.md
  popd
```

## General
* Check the version:
```bash
$ datacontract --version
datacontract version v0.3.2
```

## Options

### DuckDB
* Install DuckDB:
```bash
$ python -mpip install -U duckdb
```

* Create, or re-create the `transport_routes` view in DuckDB:
```bash
$ duckdb db.duckdb < sql/duckdb-ddl-create-view-from-csv.sql
  ls -lFh db.duckdb
-rw-r--r--  1 user  group   268K Sep 27 11:39 db.duckdb
```

* The resulting view may be queried easily
  + Schema:
```bash
$ duckdb db.duckdb "describe transport_routes;"
┌────────────────┬─────────────┬─────────┬─────────┬─────────┬───────┐
│  column_name   │ column_type │  null   │   key   │ default │ extra │
│    varchar     │   varchar   │ varchar │ varchar │ varchar │ int32 │
├────────────────┼─────────────┼─────────┼─────────┼─────────┼───────┤
│ transporter_id │ VARCHAR     │ YES     │         │         │       │
│ org_por_id     │ VARCHAR     │ YES     │         │         │       │
│ dst_por_id     │ VARCHAR     │ YES     │         │         │       │
│ freq           │ BIGINT      │ YES     │         │         │       │
└────────────────┴─────────────┴─────────┴─────────┴─────────┴───────┘
```
  + Number of records:
```bash
$ duckdb db.duckdb "select count(*) as nb_recs from transport_routes;"
┌─────────┐
│ nb_recs │
│  int64  │
├─────────┤
│   91081 │
└─────────┘
```

### Soda Core
* Install Soda Core with DuckDB:
```bash
$ python -mpip install -U soda-core-duckdb
```

* Potentially re-execute the initialization scripts of the Shell:
```bash
$ exec bash
```

* Test the connection from Soda to DuckDB:
```bash
$ soda test-connection -d duckdb_local -c soda-conf.yml -V
[12:05:22] Soda Core 3.0.50
[12:05:22] Reading configuration file "soda-conf.yml"
Successfully connected to 'duckdb_local'.
[12:05:22] Query duckdb_local.test-connection:
SELECT 1
Connection 'duckdb_local' is valid.
```

# Trouble shooting

## Soda Core
* Reference: https://github.com/sodadata/soda-core
