from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M6.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M6.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

namespace = get_namespace("http://vocab.gtfs.org/terms#")
trip_data = pd.read_csv("../data/google_transit_M6/trips.txt")
def trip_populate(data):
    id_trip = ""
    number_trips = 0
    for index, row in data.iterrows():
        if(id_trip != row['trip_id']):
            id_trip = row['trip_id']
            number_trips = number_trips + 1
            print(str(number_trips) + "/5000")
        if(number_trips > 5000):
            break
        newTrip = namespace.Trip("TripM6_" + str(index + 1))
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
        

trip_populate(trip_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M6.rdf")
