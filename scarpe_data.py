import requests
import pymysql
from bs4 import BeautifulSoup
from datetime import datetime

#SQL database variables

HOST = "localhost"
USERNAME = "root"
PASSWORD = "arnav"
DATABASE = "climate_scrape"

scrape_url = "http://103.7.130.119:8181/GenOutageReportD.aspx"

response = requests.get(scrape_url)

data = response.text

#print(data)

soup = BeautifulSoup(data, 'html.parser')

date = soup.find("input", {'id' : 'txtOnDate'})['value']

sector_type1 = "Central Sector"
sector_type2 = "State Sector"

#code for Central sector

all_stations = []
all_states = []
all_agency = []
all_unit = []
all_capa = []
all_reason = []
all_outDate = []
all_outTime = []
all_expDate = []
# stationCounter = 0
planned_table = soup.find("table", {'class' : 'planned'})
planned_trs = planned_table.findAll('tr')
counter = 0



for x in planned_trs:
        counter = counter + 1
        if counter >= 5 and counter <= 34:
                all_stations.append(x.findAll('td')[1].text.strip())
        
counter = 0
#print(planned_trs[4].findAll('td')[1].text)

#print(all_stations)

for y in planned_trs:
        counter = counter + 1
        if counter >= 5 and counter <= 34:
                all_states.append(y.findAll('td')[2].text.strip())

counter = 0

#print(all_states)

for y in planned_trs:
        counter = counter + 1
        if counter >= 5 and counter <= 34:
                all_agency.append(y.findAll('td')[3].text.strip())
                all_unit.append(y.findAll('td')[4].text.strip())
                all_capa.append(y.findAll('td')[5].text.strip())
                all_reason.append(y.findAll('td')[6].text.strip())
                all_outDate.append(y.findAll('td')[7].text.strip())
                all_outTime.append(y.findAll('td')[8].text.strip())

counter = 5

while counter <= 34:
        all_expDate.append("NULL")
        counter = counter + 1

counter = 0
#print(str(len(all_expDate)) + " " + str(len(all_stations)) + " " + str(len(all_outTime)))

#print(all_stations[0] + " " + all_states[0]  +" " + all_agency[0] + " " + all_unit[0] + " " + all_capa[0] + " " + all_reason[0] + " " + all_outDate[0] + " " + all_outTime[0])
#print()


#Code for state sector



# print(planned_trs[36].findAll('td')[1].text)
# print(planned_trs[76].findAll('td')[1].text)



all_stations_ss = []
all_states_ss = []
all_agency_ss = []
all_unit_ss = []
all_capa_ss = []
all_reason_ss = []
all_outDate_ss = []
all_outTime_ss = []
all_expDate_ss = []

counter = 0

for y in planned_trs:
        counter = counter + 1
        if counter >= 37 and counter <= 77:
                all_stations_ss.append(y.findAll('td')[1].text.strip())
                all_states_ss.append(y.findAll('td')[2].text.strip())
                all_agency_ss.append(y.findAll('td')[3].text.strip())
                all_unit_ss.append(y.findAll('td')[4].text.strip())
                all_capa_ss.append(y.findAll('td')[5].text.strip())
                all_reason_ss.append(y.findAll('td')[6].text.strip())
                all_outDate_ss.append(y.findAll('td')[7].text.strip())
                all_outTime_ss.append(y.findAll('td')[8].text.strip())

counter = 37

while counter <= 77:
        all_expDate_ss.append("NULL")
        counter = counter + 1

counter = 0

#print(all_stations_ss[0] + " " + all_states_ss[0]  +" " + all_agency_ss[0] + " " + all_unit_ss[0] + " " + all_capa_ss[0] + " " + all_reason_ss[0] + " " + all_outDate_ss[0] + " " + all_outTime_ss[0])
#print(all_stations_ss[40] + " " + all_states_ss[40]  +" " + all_agency_ss[40] + " " + all_unit_ss[40] + " " + all_capa_ss[40] + " " + all_reason_ss[40] + " " + all_outDate_ss[40] + " " + all_outTime_ss[40])


#print(str(len(all_expDate_ss)) + " " + str(len(all_stations_ss)) + " " + str(len(all_outTime_ss)))



# add list to database

db = pymysql.connect(HOST, USERNAME, PASSWORD, DATABASE)

cursor = db.cursor()

# cursor.execute("DROP TABLE IF EXISTS planned_out")

# sql = """CREATE TABLE planned_out (
# 	date varchar(255),
#     sector_type varchar(255),
#     station varchar(255),
#     states varchar(255),
#     agency varchar(255),
#     unit_no varchar(255),
#     capacity varchar(255),
#     reason varchar(255),
#     outage_date varchar(255),
#     outage_time varchar(255),
#     expected_revival_date varchar(255),
#     inserted_at varchar(255)
# )"""

# cursor.execute(sql)

counter = 0

def getCurrTime():
        now = datetime.now()
        dt_string1 = now.strftime("%Y/%m/%d %H:%M:%S")
        return dt_string1

while counter < 30:
        cursor.execute("INSERT INTO planned_out VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, sector_type1, all_stations[counter], all_states[counter], all_agency[counter], all_unit[counter], all_capa[counter], all_reason[counter], all_outDate[counter], all_outTime[counter], all_expDate[counter] ,getCurrTime() ))
        counter = counter + 1

counter = 0

while counter < 41:
        cursor.execute("INSERT INTO planned_out VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (date, sector_type2, all_stations_ss[counter], all_states_ss[counter], all_agency_ss[counter], all_unit_ss[counter], all_capa_ss[counter], all_reason_ss[counter], all_outDate_ss[counter], all_outTime_ss[counter], all_expDate_ss[counter] ,getCurrTime() ))
        counter = counter + 1




