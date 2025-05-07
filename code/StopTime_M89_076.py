from owlready2 import *;
import pandas as pd;
from datetime import datetime;
import os;
import re;


if os.path.exists("../ontologies/publicTransportMadrid_M89_076.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M89_076.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

stop_time_data = pd.read_csv("../data/google_transit_M89/20250327_google_transit_M89_076/stop_times.txt")
namespace = get_namespace("http://vocab.gtfs.org/terms#")

def string_to_hour(date):
    if(date[:2]=="24"):
        date = date.replace(date[:2], "00")
    if(date[:2]=="25"):
        date = date.replace(date[:2], "01")
    result = datetime.strptime(date, '%H:%M:%S').time()
    return result 

def stop_time_populate(data):
    for index, row in data.iterrows():
        newStopTime = namespace.StopTime("StopTimeM89_76_" + str(index + 1))
        for i in ontology.Stop.instances():

            if(row['stop_id'] == i.hasId[0]):
                newStopTime.stopPerformedAt.append(i)
            
        for i in namespace.Trip.instances():

            if(row['trip_id'] == i.hasId[0]):
                newStopTime.stopPerformedDuringTrip.append(i)
                break
        newStopTime.arrivalTime.append(string_to_hour(row['arrival_time']))
        newStopTime.departureTime.append(string_to_hour(row['departure_time']))
        newStopTime.stopSequence.append(row['stop_sequence'])
        print(str(index+1) + "/" + str(len(data)))

stop_time_populate(stop_time_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M89_076.rdf")