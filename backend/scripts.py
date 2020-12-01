# This python file gather all utilities functions which are necessary
import networkx as nx
import json
import numpy as np
from collections import Counter


f = open("backend\\dimension_name.txt")


list_dimension_name = [(str(line.rstrip()), index)
                       for index, line in enumerate(f)]

dict_dimension_name = dict(list_dimension_name)

# Return sorterd top k of values of dictionnary
# with k,v = article_name,article_score
def sorted_top_k(dico,top_tk):
    k = Counter(dico)
    top_k = k.most_common(top_tk)
    return top_k
    

# Create query vector of 299 items 
def vectorize_query(query):
    vector = [0]*299
    # query = string_to_list(query)
    list_type = get_list_type(query)
    # print(list_type)
    list_index = get_list_index(list_type)
    # print(list_index)
    for index in list_index:
        vector[int(index)] = 1
    return vector

# Create a list of term by splitting string 

def string_to_list(query):
    return query.split(" ")

# For each term in the query, return its typeid_name
# example : for tern "capital" -> type = <wordnet_capital_108518505>

def get_list_type(query):
    with open("backend\\typeid_name.json") as ids:
        typeid_name = json.load(ids)
        list_type = []
        for keyword in query:
            if keyword in typeid_name:
                list_type.append(str(typeid_name.get(keyword).get('type')))
        return list_type

# For each type in list_type, returns its index according to 
# dimension_name.txt file
# example : 
# list_type  = ['<wordnet_capital_108518505>', '<wordnet_city_108524735>', '<wordnet_company_108058098>']
# list_index = [['274', '260', '169']

def get_list_index(list_type):        
    list_index = []
    for t in list_type:
        if (str(t) in dict_dimension_name.keys()):
            list_index.append(str(dict_dimension_name.get(str(t))))
    return list_index


# Build a tree in python through recursion by taking in json object
# inspired from source code from https://stackoverrun.com/fr/q/4120975
# This class represent a node
class node:
    def _init_(self, name=None, children=None):
        self.name = name
        if children is None:
            self.children = []
        else:
            self.children = children

    def getName(self):
        return self.name

    def getChildren(self):
        childrens = []
        for children in self.children:
            childrens.append(children.name)
        return childrens

# Tree class : represent json as tree
class tree:
    nodes = []
    def buildnode(self, ob):
        node1 = node()
        node1.name = ob['name']
        node1.children = []
        if "children" in ob:
            for children in ob['children']:
                node1.children.append(self.buildnode(children))
        self.nodes.append(node1)
        return node1

    def getNodes(self):
        return self.nodes

# Build a graph according to list of node


def createGraph(nodes):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node.name)
    for node in nodes:
        for children in node.children:
            G.add_edge(node.name, children.name)
    return G
