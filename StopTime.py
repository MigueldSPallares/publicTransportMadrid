from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("D:/publicTransport/publicTransportMadrid_full.rdf"):
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid_full.rdf").load()
else:
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid.rdf").load()

#En caso de descargarlo, cambiad el directorio a la dirección de los archivos

stop_time_data = pd.read_csv("D:/publicTransport/data/google_transit_M4/stop_times.txt")

def stop_time_populate(data):
    for index, row in data.iterrows():
        stopTimeId = row['trip_id'] + str(row['stop_sequence'])
        newStopTime = ontology.StopTime(stopTimeId)
        for i in ontology.Stop.instances():
            parts = str(i).split(".")
            if(row['stop_id'] == parts[1]):
                newStopTime.stopPerformedAt.append(i)
            
        for i in ontology.Trip.instances():
            parts = str(i).split(".")
            if(row['trip_id'] == parts[1]):
                newStopTime.stopPerformedDuringTrip.append(i)
        newStopTime.arrivalTime.append(row['arrival_time'])

stop_time_populate(stop_time_data)

ontology.save(file = "D:/publicTransport/publicTransportMadrid_full.rdf")