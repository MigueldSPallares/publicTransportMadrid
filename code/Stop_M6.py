from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M6.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M6.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

stop_data = pd.read_csv("../data/google_transit_M6/stops.txt")


def stop_populate(data):
    for index, row in data.iterrows():
        if(row['location_type']== 0):
            newStop = ontology.NormalStop("StopM6_" + str(index+1))
        elif(row['location_type']== 1):
            newStop = ontology.Station("StopM6_" + str(index+1))
        elif(row['location_type'] == 2):
            newStop = ontology.Entrance_Exit("StopM6_" + str(index+1))
        elif(row['location_type'] == 3):
            newStop = ontology.GenericNode("StopM6_" + str(index+1))
        elif(row['location_type'] == 4):
            newStop = ontology.BoardingArea("StopM6_" + str(index+1))
        newStop.hasId.append(row['stop_id'])
        newStop.hasName.append(row['stop_name'])
        if((pd.isnull(row['stop_desc']))==False):
            newStop.hasDescription.append(row['stop_desc'])
        newStop.latitude.append(row['stop_lat'])
        newStop.longitude.append(row['stop_lon'])
        if(row['wheelchair_boarding'] == 0):
            newStop.stopIsWheelchairAccesible.append(ontology.WheelchairAccesibilityUnknown)
        if(row['wheelchair_boarding'] == 1):
            newStop.stopIsWheelchairAccesible.append(ontology.IsWheelchairAccesible)
        if(row['wheelchair_boarding'] == 2):
            newStop.stopIsWheelchairAccesible.append(ontology.IsNotWheelchairAccesible)
        print(str(index+1) + "/" + str(len(data)))

stop_populate(stop_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M6.rdf")
