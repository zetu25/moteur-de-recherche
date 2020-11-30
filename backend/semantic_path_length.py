import networkx as nx
import json
from scripts import *
import jsonpickle
from article import Article

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

class implementation:
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


def createGraph(nodes):
    G = nx.Graph()
    for node in nodes:
        G.add_node(node.name)
    for node in nodes:
        for children in node.children:
            G.add_edge(node.name, children.name)
    return G

# Get path length between two entities
def getPathLen(G, first, second):
    # print(shortest_path_dictionnary[first][second]+1)
    return shortest_path_dictionnary[first][second]+1


def getSimPath(pathlen):
    return 1/pathlen


def getHighestValue(q, document):
    highest = 0

    for i in document:
        pathlen = getPathLen(G, q, i)

        simpathlen = getSimPath(pathlen)
        if simpathlen > highest:
            highest = simpathlen
    return highest

##Moyenne des plus grandes valeurs


def getMeanValue(query, document):
    liste = []
    for q in query:
         h = getHighestValue(q, document)

         liste.append(h)
    
    return (sum(liste) / len(liste))


def getPathLengthSimilarity(entities,top_k):
    results = dict()
    with open('backend\\article_typeid.json') as article_vector:
        articles = json.load(article_vector)

        for article in articles:
            score = getMeanValue(entities, articles[article])
            results[article] = score
    result = [Article(title, score)
              for (title, score) in sorted_top_k(results, top_tk)]
    return str(jsonpickle.encode(result, unpicklable=False))


f = open("backend\\ontology.json")
data = json.load(f)
builder = implementation()
builder.buildnode(data)

nodes = builder.getNodes()
G = createGraph(nodes)
shortest_path_dictionnary = dict(nx.all_pairs_shortest_path_length(G))

if __name__ == "__main__":
    print(getPathLengthSimilarity(['entity', 'person', 'organization', 'event'],10))
