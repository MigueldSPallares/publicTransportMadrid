from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("D:/publicTransport/publicTransportMadrid_full.rdf"):
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid_full.rdf").load()
else:
    ontology = get_ontology("D:/publicTransport/publicTransportMadrid.rdf").load()

route_data = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/routes.txt")

def route_populate(data):
    for index, row in data.iterrows():
        if(row['route_id'][:2]== "4_"):
            newRoute = ontology.MetroRoute(("Route" + str(row['route_id'])))
            newRoute.hasName.append(row['route_long_name'])
            newRoute.hasUrl.append(row['route_url'])
        if(row['route_id'][:2]== "5_"):
            newRoute = ontology.CercaniasRoute(("Route" + str(row['route_id'])))
            newRoute.hasName.append(row['route_long_name'])
            newRoute.hasUrl.append(row['route_url'])
        if(row['route_id'][:2]== "6_"):
            newRoute = ontology.EMTBusRoute(("Route" + str(row['route_id'])))
            newRoute.hasName.append(row['route_long_name'])
            newRoute.hasUrl.append(row['route_url'])
        if(row['route_id'][:2]== "8_"):
            newRoute = ontology.InterurbanBusRoute(("Route" + str(row['route_id'])))
            newRoute.hasName.append(row['route_long_name'])
            newRoute.hasUrl.append(row['route_url'])
        if(row['route_id'][:2]== "9_"):
            newRoute = ontology.OtherUrbanRoute(("Route" + str(row['route_id'])))
            newRoute.hasName.append(row['route_long_name'])
            newRoute.hasUrl.append(row['route_url'])
        if(row['route_id'][:3]== "10_"):
            newRoute = ontology.LightrailRoute(("Route" + str(row['route_id'])))
            newRoute.hasName.append(row['route_long_name'])
            newRoute.hasUrl.append(row['route_url'])
      
route_populate(route_data)

ontology.save(file = "D:/publicTransportMadrid_full.rdf")
