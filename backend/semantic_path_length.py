import json
from scripts import *
import jsonpickle
from article import Article


f = open("backend\\ontology.json")
data = json.load(f)
builder = tree()
builder.buildnode(data)

nodes = builder.getNodes()
G = createGraph(nodes)
shortest_path_dictionnary = dict(nx.all_pairs_shortest_path_length(G))
f.close()

# Get path length between two entities
def get_terms_path_length(first, second):
    return shortest_path_dictionnary[first][second]+1

# Return simPath value
def get_sim_path(pathlen):
    return 1/pathlen

# Return the highest simPath value
def get_highest_value(term, document):
    highest = 0
    for doc_term in document:
        pathlen = get_terms_path_length(term, doc_term)
        simpathlen = get_sim_path(pathlen)
        if simpathlen > highest:
            highest = simpathlen
    return highest

# Mean of all the highest selected score
def get_mean_value(query, document):
    liste = []
    for q in query:
         h = get_highest_value(q, document)
         liste.append(h)
    
    return (sum(liste) / len(liste))

# Return top_k path_legth similar doc to the query
def get_path_length_similarity(query,top_k):
    article_scores = dict()
    with open('backend\\article_typeid.json') as article_vector:
        articles = json.load(article_vector)

        for article in articles:
            score = get_mean_value(query, articles[article])
            article_scores[article] = score
    res = [Article(title, score)
           for (title, score) in sorted_top_k(article_scores, top_k)]
    return str(jsonpickle.encode(res, unpicklable=False))


if __name__ == "__main__":
    # print(get_terms_path_length(G,'entity', 'ruler.king'))
    
    print(get_path_length_similarity(
        ['entity', 'person', 'organization', 'event'], 10))
