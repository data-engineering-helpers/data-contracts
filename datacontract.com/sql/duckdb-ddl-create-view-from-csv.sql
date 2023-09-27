--
-- File: https://github.com/data-engineering-helpers/data-contracts/tree/main/datacontract.com/sql/duckdb-ddl-create-view-from-csv.sql
--

drop view if exists transport_routes;

create view transport_routes as (
  select *
  from read_csv_auto("data/optd/optd_airline_por.csv",
                     header=True,
                     delim="^",
                     AUTO_DETECT=TRUE)
);


