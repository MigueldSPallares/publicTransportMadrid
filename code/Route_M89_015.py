from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M89_015.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M89_015.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

route_data = pd.read_csv("../data/google_transit_M89/20250329_google_transit_M89_015/routes.txt")

def route_populate(data):
    for index, row in data.iterrows():
        if(row['route_id'][:2]== "8_"):
            newRoute = ontology.InterurbanBusRoute("RouteM89_15_" + str(index+1))
        if(row['route_id'][:2]== "9_"):
            newRoute = ontology.UrbanBusRoute("RouteM89_15_" + str(index+1))
        newRoute.hasId.append(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
        newRoute.hasTransportMethod.append(ontology.Bus)
        print(str(index+1) + "/" + str(len(data)))
      
route_populate(route_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M89_015.rdf")