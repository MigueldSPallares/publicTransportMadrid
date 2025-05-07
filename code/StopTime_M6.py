from owlready2 import *;
import pandas as pd;
from datetime import datetime;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M6.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M6.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

#En caso de descargarlo, cambiad el directorio a la dirección de los archivos

stop_time_data = pd.read_csv("../data/google_transit_M6/stop_times.txt")
namespace = get_namespace("http://vocab.gtfs.org/terms#")

def string_to_hour(date):
    if(date[:2]=="24"):
        date = date.replace(date[:2], "00")
    result = datetime.strptime(date, '%H:%M:%S').time()
    return result 

def stop_time_populate(data):
    id_trip = ""
    number_trips = 0
    for index, row in data.iterrows():
        if(id_trip != row['trip_id']):
            id_trip = row['trip_id']
            number_trips = number_trips + 1
            print(str(number_trips) + "/5000")
        if(number_trips > 5000):
            break
        newStopTime = namespace.StopTime("StopTimeM6_" + str(index + 1))
        for i in ontology.Stop.instances():
            if(row['stop_id'] == i.hasId[0]):
                newStopTime.stopPerformedAt.append(i)
                break
        for i in namespace.Trip.instances():
            if(row['trip_id'] == i.hasId[0]):
                newStopTime.stopPerformedDuringTrip.append(i)
                break
        newStopTime.arrivalTime.append(string_to_hour(row['arrival_time']))
        newStopTime.departureTime.append(string_to_hour(row['departure_time']))
        newStopTime.stopSequence.append(row['stop_sequence'])
        
        

stop_time_populate(stop_time_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M6.rdf")
