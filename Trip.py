from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("D:/publicTransport/publicTransportMadrid_full.rdf"):
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid_full.rdf").load()
else:
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid.rdf").load()

namespace = get_namespace("http://vocab.gtfs.org/terms#")
trip_data = pd.read_csv("D:/publicTransport/data/google_transit_M4/trips.txt")
def trip_populate(data):

    for index, row in data.iterrows():
        newTrip = ontology.Trip(row['trip_id'])
        newTrip.hasName.append(row['trip_short_name'])
        for i in namespace.Service.instances():
            parts = str(i).split(".")
            if(row['service_id'] == parts[1]):
                newTrip.performedByService.append(i)
            
        for i in ontology.Route.instances():
            parts = str(i).split(".")
            if(row['service_id'] == parts[1]):
                newTrip.goesThroughRoute.append(i)
        if(row['wheelchair_accessible'] == 0):
            newTrip.isWheelchairAccesible.append(ontology.wheelchairAccesibilityUnknown)
        if(row['wheelchair_accessible'] == 1):
            newTrip.isWheelchairAccesible.append(ontology.IsWheelchairAccesible)
        if(row['wheelchair_accessible'] == 2):
            newTrip.isWheelchairAccesible.append(ontology.IsNotWheelchairAccesible)

trip_populate(trip_data)

ontology.save(file = "D:/publicTransport/publicTransportMadrid_full.rdf")
