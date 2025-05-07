from owlready2 import *;
import pandas as pd;
from datetime import datetime;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M89_042.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M89_042.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

stop_time_data = pd.read_csv("../data/google_transit_M89/20250328_google_transit_M89_042/stop_times.txt")
namespace = get_namespace("http://vocab.gtfs.org/terms#")

def string_to_hour(date):
    if(date[:2]=="24"):
        date = date.replace(date[:2], "00")
    if(date[:2]=="25"):
        date = date.replace(date[:2], "01")
    if(date[:2]=="26"):
        date = date.replace(date[:2], "02")
    result = datetime.strptime(date, '%H:%M:%S').time()
    return result 

def stop_time_populate(data):
    for index, row in data.iterrows():
        newStopTime = namespace.StopTime("StopTimeM89_42_" + str(index + 1))
        for i in ontology.Stop.instances():
            parts = str(i).split(".")
            if(row['stop_id'] == i.hasId[0]):
                newStopTime.stopPerformedAt.append(i)
            
        for i in namespace.Trip.instances():
            parts = str(i).split(".")
            if(row['trip_id'] == i.hasId[0]):
                newStopTime.stopPerformedDuringTrip.append(i)
                break
        newStopTime.arrivalTime.append(string_to_hour(row['arrival_time']))
        newStopTime.departureTime.append(string_to_hour(row['departure_time']))
        newStopTime.stopSequence.append(row['stop_sequence'])
        print(str(index+1) + "/" + str(len(data)))

stop_time_populate(stop_time_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M89_042.rdf")