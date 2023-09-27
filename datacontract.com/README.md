Data Contracts - Datacontract.com
=================================

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
* If not already done so, clone this Git repository and change directory to it:
```bash
$ mkdir -p ~/dev/infra/data-contracts && \
  git clone https://github.com/data-engineering-helpers/data-contracts.git ~/dev/infra/data-contracts/data-contracts && \
  cd ~/dev/infra/data-contracts/data-contracts/datacontract.com
```

* Check the validity of the data contract:
```bash
$ datacontract lint --file contracts/data-contract-flight-route.yaml
🟢 data contract is valid!
```

* Open the data contract in Data Contract Studio:
```bash
$ datacontract open --file contracts/data-contract-flight-route.yaml
🌐 opening data contract at https://studio.datacontract.com/s/16ff8cbb-7f3f-4ca4-addf-b3a4cbac1500
```
  + Which results, for
    [`contracts/data-contract-flight-route.yaml`](https://github.com/data-engineering-helpers/data-contracts/tree/main/datacontract.com/contracts/data-contract-flight-route.yaml),
	into
    https://studio.datacontract.com/s/16ff8cbb-7f3f-4ca4-addf-b3a4cbac1500

* Generate a new data contract:
```bash
$ datacontract init --file contracts/orders-latest-npii-new.yaml
📄 data contract written to contracts/orders-latest-npii-new.yaml
```

* Open the newly created data contract in Data Contract Studio:
```bash
$ datacontract open --file contracts/orders-latest-npii-new.yaml
🌐 opening data contract at https://studio.datacontract.com/s/c8b27fe3-62dc-4a21-ae41-9471ce7859d7
```

* The data contract may be edited in Data Contract Studio directly:
  https://studio.datacontract.com/s/c8b27fe3-62dc-4a21-ae41-9471ce7859d7/edit

* Create a local replication of some existing data contract in
  Data Contract Studio:
```bash
$ datacontract init --from https://studio.datacontract.com/s/c8b27fe3-62dc-4a21-ae41-9471ce7859d7.yaml
📄 data contract written to datacontract.yaml
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
datacontract version v0.2.0
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

* Launch a few sample checks:
```bash
$ soda scan -d duckdb_local -c soda-conf.yml soda-checks.yml
[16:16:10] Soda Core 3.0.50
[16:16:11] Scan summary:
[16:16:11] 2/2 checks PASSED: 
[16:16:11]     transport_routes in duckdb_local
[16:16:11]       row_count between 90000 and 100000 [PASSED]
[16:16:11]       invalid_percent(freq) = 0 % [PASSED]
[16:16:11] All is good. No failures. No warnings. No errors.
```

# Trouble shooting

## Soda Core
* Reference: https://github.com/sodadata/soda-core