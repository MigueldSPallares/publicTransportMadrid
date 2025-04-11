from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("D:/publicTransportMadrid_full.rdf"):
    ontology = get_ontology("D:/publicTransportMadrid_full.rdf").load()
else:
    ontology = get_ontology("D:/publicTransportMadrid.rdf").load()

data = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/routes.txt")

for index, row in data.iterrows():
    
    if(row['route_id'][:2]== "4_"):
        newRoute = ontology.MetroRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:2]== "5_"):
        newRoute = ontology.CercaniasRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:2]== "6_"):
        newRoute = ontology.EMTBusRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:2]== "8_"):
        newRoute = ontology.InterurbanBusRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:2]== "9_"):
        newRoute = ontology.OtherUrbanRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:2]== "10_"):
        newRoute = ontology.LightrailRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
      

ontology.save(file = "D:/publicTransportMadrid_full.rdf")
