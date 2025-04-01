from owlready2 import *;
import pandas as pd;


ontology = get_ontology("D:/publicTransportMadrid.rdf").load()

data = pd.read_csv("C:/Users/migue/Downloads/google_transit_M4/trips.txt")

print(list(ontology.Stop.subclasses()))



for index, row in data.iterrows():
        for i in ontology.Service.instances():
            parts = str(i).split(".")
        for i in ontology.Routes.instances():
            parts = str(i).split(".")