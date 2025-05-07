from owlready2 import *;
import pandas as pd;
from datetime import datetime;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M89_030.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M89_030.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

namespace = get_namespace("http://vocab.gtfs.org/terms#")

data_calendar = pd.read_csv("../data/google_transit_M89/20250328_google_transit_M89_030/calendar.txt")
data_calendar_dates = pd.read_csv("../data/google_transit_M89/20250328_google_transit_M89_030/calendar_dates.txt")
def number_to_date(date):
    int_to_string = str(date)
    string_date = int_to_string[0:4] + "-" + int_to_string[4:6] + "-" + int_to_string[6:8]
    result = datetime.strptime(string_date, '%Y-%m-%d').date()
    return result 

def service_populate(calendar_data, calendar_dates_data):
    for index, row in calendar_data.iterrows():
        service = namespace.Service("ServiceM89_30_" + str(index+1))
        service.hasId.append(row['service_id'])
        if(row["monday"] == 1):
            service.isAvailableAtDay.append(ontology.Monday)
        if(row["tuesday"] == 1):
            service.isAvailableAtDay.append(ontology.Tuesday)
        if(row["wednesday"] == 1):
            service.isAvailableAtDay.append(ontology.Wednesday)
        if(row["thursday"] == 1):
            service.isAvailableAtDay.append(ontology.Thursday)
        if(row["friday"] == 1):
            service.isAvailableAtDay.append(ontology.Friday)
        if(row["saturday"] == 1):
            service.isAvailableAtDay.append(ontology.Saturday)
        if(row["sunday"] == 1):
            service.isAvailableAtDay.append(ontology.Sunday)
        service.startService.append(number_to_date(row['start_date']))
        service.endService.append(number_to_date(row['end_date']))
        print(str(index+1) + "/" + str(len(calendar_data)))
    for index, row in calendar_dates_data.iterrows():
        for i in namespace.Service.instances():
            id = str(i).split(".")
            if(i.hasId[0] == (row['service_id'])):
                
                if(row['exception_type'] == 1):
                    i.serviceExceptionAvailableAt.append(number_to_date(row['date']))
                    
                if(row['exception_type'] == 2):
                    i.serviceExceptionNotAvailableAt.append(number_to_date(row['date']))
        print(str(index+1) + "/" + str(len(calendar_dates_data)))

service_populate(data_calendar, data_calendar_dates)

ontology.save(file = "../ontologies/publicTransportMadrid_M89_030.rdf")