from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("D:/publicTransport/publicTransportMadrid_full.rdf"):
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid_full.rdf").load()
else:
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid.rdf").load()

stop_data = pd.read_csv("D:/publicTransport/data/google_transit_M4/stops.txt")


def stop_populate(data):
    for index, row in data.iterrows():
        
        if(row['location_type']== 1):
            newStop = ontology.Station(row['stop_id'])
            newStop.hasName.append(row['stop_name'])
            newStop.hasDescription.append(row['stop_desc'])
            newStop.latitude.append(row['stop_lat'])
            newStop.longitude.append(row['stop_lon'])
    
    for index, row in data.iterrows():
        if(row['location_type']== 0):
            newStop = ontology.NormalStop(row['stop_id'])
        elif(row['location_type'] == 2):
            newStop = ontology.Entrance_Exit(row['stop_id'])
        elif(row['location_type'] == 3):
            newStop = ontology.GenericNode(row['stop_id'])
        elif(row['location_type'] == 4):
            newStop = ontology.BoardingArea(row['stop_id'])
        
        newStop.hasName.append(row['stop_name'])
        if((pd.isnull(row['stop_desc']))==False):
            newStop.hasDescription.append(row['stop_desc'])
        newStop.latitude.append(row['stop_lat'])
        newStop.longitude.append(row['stop_lon'])
        if(row['wheelchair_boarding'] == 0):
            newStop.isWheelchairAccesible.append(ontology.wheelchairAccesibilityUnknown)
        if(row['wheelchair_boarding'] == 1):
            newStop.isWheelchairAccesible.append(ontology.IsWheelchairAccesible)
        if(row['wheelchair_boarding'] == 2):
            newStop.isWheelchairAccesible.append(ontology.IsNotWheelchairAccesible)

stop_populate(stop_data)

ontology.save(file = "D:/publicTransport/publicTransportMadrid_full.rdf")
