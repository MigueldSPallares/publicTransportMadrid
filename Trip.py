from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("D:/publicTransportMadrid_full.rdf"):
    ontology = get_ontology("D:/publicTransportMadrid_full.rdf").load()
else:
    ontology = get_ontology("D:/publicTransportMadrid.rdf").load()

data = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/trips.txt")
data_1 = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/calendar.txt")
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

for index, row in data.iterrows():
    newTrip = ontology.Trip(row['trip_id'])
    newTrip.hasName.append(row['trip_short_name'])
    for i in ontology.Service.instances():
        parts = str(i).split(".")
        if(row['service_id'] == parts[1]):
            newTrip.performedByService.append(i)
        
    for i in ontology.Route.instances():
        parts = str(i).split(".")
        if(row['service_id'] == parts[1]):
            newTrip.goesThroughRoute.append(i)
    if(row['wheelchair_boarding'] == 0):
        newTrip.isWheelchairAccesible.append(ontology.wheelchairAccesibilityUnknown)
    if(row['wheelchair_boarding'] == 1):
        newTrip.isWheelchairAccesible.append(ontology.IsWheelchairAccesible)
    if(row['wheelchair_boarding'] == 2):
        newTrip.isWheelchairAccesible.append(ontology.IsNotWheelchairAccesible)

ontology.save(file = "D:/publicTransportMadrid_full.rdf")
