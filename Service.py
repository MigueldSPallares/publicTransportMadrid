from owlready2 import *;
import pandas as pd;
from datetime import datetime;
import os;


if os.path.exists("D:/publicTransport/publicTransportMadrid_full.rdf"):
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid_full.rdf").load()
else:
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid.rdf").load()

namespace = get_namespace("http://vocab.gtfs.org/terms#")

data_calendar = pd.read_csv("D:/publicTransport/data/google_transit_M4/calendar.txt")
data_calendar_dates = pd.read_csv("D:/publicTransport/data/google_transit_M4/calendar_dates.txt")
def number_to_date(date):
    int_to_string = str(date)
    string_date = int_to_string[0:4] + "-" + int_to_string[4:6] + "-" + int_to_string[6:8]
    result = datetime.strptime(string_date, '%Y-%m-%d').date()
    return result 

def service_populate(calendar_data, calendar_dates_data):
    for index, row in calendar_data.iterrows():
        service = namespace.Service(("Service_" + str(row['service_id'])))
        if(row["monday"] == 1):
            service.isAvailableAtDay.append("Monday")
        if(row["tuesday"] == 1):
            service.isAvailableAtDay.append("Tuesday")
        if(row["wednesday"] == 1):
            service.isAvailableAtDay.append("Wednesday")
        if(row["thursday"] == 1):
            service.isAvailableAtDay.append("Thursday")
        if(row["friday"] == 1):
            service.isAvailableAtDay.append("Friday")
        if(row["saturday"] == 1):
            service.isAvailableAtDay.append("Saturday")
        if(row["sunday"] == 1):
            service.isAvailableAtDay.append("Sunday")
        service.hasName.append(row['service_id'])
        service.startService.append(number_to_date(row['start_date']))
        service.endService.append(number_to_date(row['end_date']))
    for index, row in calendar_dates_data.iterrows():
        for i in namespace.Service.instances():
            if(row['service_id'] == i.hasName[0]):
                
                if(row['exception_type'] == 1):
                    i.serviceExecptionAvailableAt.append(number_to_date(row['date']))
                    
                if(row['exception_type'] == 2):
                    i.serviceExceptionNotAvailableAt.append(number_to_date(row['date']))

service_populate(data_calendar, data_calendar_dates)

ontology.save(file = "D:/publicTransport/publicTransportMadrid_full.rdf")
