from owlready2 import *;
import pandas as pd;


ontology = get_ontology("D:/publicTransportMadrid.rdf").load()

data_1 = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/calendar.txt")
data_2 = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/calendar_dates.txt")
print(data_1)

def date_to_string(date):
    int_to_string = str(date)
    newDate = int_to_string[0:4] + "-" + int_to_string[4:6] + "-" + int_to_string[6:8]
    return newDate

for index, row in data_1.iterrows():
    if(row['service_id'].startswith("4_")):
        
        service = ontology.Service(row['service_id'])
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
        service.startService.append(date_to_string(row['start_date']))
        service.endService.append(date_to_string(row['end_date']))
        


for index, row in data_2.iterrows():
        for i in ontology.Service.instances():
            parts = str(i).split(".")
            if(row['service_id'] == parts[1]):
                if(row['exception_type'] == 1):
                    i.serviceExecptionAvailableAt.append(date_to_string(row['date']))
                    print(date_to_string(row['date']))
                if(row['exception_type'] == 2):
                    i.serviceExceptionNotAvailableAt.append(date_to_string(row['date']))

print(list(default_world.sparql("""
           SELECT ?x ?isAvailableException ?startDate
           { ?service rdfs:subClassOf* publicTransportMadrid:Service .
             ?x rdf:type ?service;
                publicTransportMadrid:serviceExecptionAvailableAt ?isAvailableException;
                publicTransportMadrid:startService ?startDate . }
    """)))
        
