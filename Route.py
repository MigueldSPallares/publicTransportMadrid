from owlready2 import *;
import pandas as pd;


ontology = get_ontology("D:/publicTransportMadrid.rdf").load()

data = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/routes.txt")



for index, row in data.iterrows():
    if(row['route_id'][:3]== "4__"):
        newRoute = ontology.MetroRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:3]== "5__"):
        newRoute = ontology.MetroRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:3]== "6__"):
        newRoute = ontology.MetroRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:3]== "8__"):
        newRoute = ontology.MetroRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:3]== "9__"):
        newRoute = ontology.MetroRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
    if(row['route_id'][:3]== "10__"):
        newRoute = ontology.MetroRoute(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
      
print(list(default_world.sparql("""
           SELECT ?x ?name ?url
           { ?s rdfs:subClassOf* publicTransportMadrid:MetroRoute .
             ?x rdf:type ?s;
                  publicTransportMadrid:hasName ?name;
                  publicTransportMadrid:hasUrl ?url  . FILTER (?name = 'Circular') }
    """)))

print(list(ontology.data_properties()))
