--
-- File: https://github.com/data-engineering-helpers/data-contracts/tree/main/datacontract.com/sql/duckdb-ddl-create-view-from-csv.sql
--

drop view if exists transport_routes;

create view transport_routes as (
  select airline_code as transporter_id,
  		 apt_org as org_por_id,
  		 apt_dst as dst_por_id,
		 flt_freq as freq
  from read_csv_auto("data/optd/optd_airline_por.csv",
                     header=True,
                     delim="^",
                     AUTO_DETECT=TRUE)
);

