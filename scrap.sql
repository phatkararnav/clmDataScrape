CREATE DATABASE scrape_data;

CREATE TABLE planned_out (
	date varchar(255),
    sector_type varchar(255),
    station varchar(255),
    states varchar(255),
    agency varchar(255),
    unit_no varchar(255),
    capacity varchar(255),
    reason varchar(255),
    outage_date varchar(255),
    outage_time varchar(255),
    expected_revival_date varchar(255),
    inserted_at varchar(255)
);


--INSERT INTO planned_out VALUES ('28-05-2020', 'Central Sector', 'SKS Power', 'Chhattisgarh', 'SKS', '2', 300, 'Low Schedule', '07-07-2019', '00:18', 'NULL', '22:22:22:22' )

--"INSERT INTO planned_out VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, sector_type2, all_stations_ss[counter], all_states_ss[counter], all_agency_ss[counter], all_unit_ss[counter], all_capa_ss[counter], all_reason_ss[counter], all_outDate_ss[counter], all_outTime_ss[counter], all_expDate_ss[counter] ,getCurrTime() )
