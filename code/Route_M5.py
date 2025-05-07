from owlready2 import *;
import pandas as pd;
import os;


if os.path.exists("../ontologies/publicTransportMadrid_M5.rdf"):
    ontology = get_ontology("../ontologies/publicTransportMadrid_M5.rdf").load()
else:
    ontology = get_ontology("../ontologies/publicTransportMadrid.rdf").load()

route_data = pd.read_csv("../data/google_transit_M5/routes.txt")

def route_populate(data):
    for index, row in data.iterrows():
        newRoute = ontology.CercaniasRoute("RouteM5_" + str(index+1))
        newRoute.hasId.append(row['route_id'])
        newRoute.hasName.append(row['route_long_name'])
        newRoute.hasUrl.append(row['route_url'])
        newRoute.hasTransportMethod.append(ontology.Rail)
        print(str(index+1) + "/" + str(len(data)))
      
route_populate(route_data)

ontology.save(file = "../ontologies/publicTransportMadrid_M5.rdf")