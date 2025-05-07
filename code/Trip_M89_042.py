from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M89_042.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M89_042.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

namespace = get_namespace("http://vocab.gtfs.org/terms#")
trip_data = pd.read_csv("../data/google_transit_M89/20250328_google_transit_M89_042/trips.txt")
def trip_populate(data):

    for index, row in data.iterrows():
        newTrip = namespace.Trip("TripM89_42_" + str(index + 1))
        newTrip.hasId.append(row['trip_id'])
        newTrip.hasName.append(row['trip_short_name'])
        for i in namespace.Service.instances():
            parts = str(i).split(".")
            
            if((row['service_id']) == i.hasId[0]):
                newTrip.performedByService.append(i)
                break
            
        for i in ontology.Route.instances():
            parts = str(i).split(".")
            if(row['route_id'] == i.hasId[0]):
                newTrip.performedAtRoute.append(i)
                break
        if(row['wheelchair_accessible'] == 0):
            newTrip.tripIsWheelchairAccesible.append(ontology.WheelchairAccesibilityUnknown)
        if(row['wheelchair_accessible'] == 1):
            newTrip.tripIsWheelchairAccesible.append(ontology.IsWheelchairAccesible)
        if(row['wheelchair_accessible'] == 2):
            newTrip.tripIsWheelchairAccesible.append(ontology.IsNotWheelchairAccesible)
        print(str(index+1) + "/" + str(len(data)))

trip_populate(trip_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M89_042.rdf")