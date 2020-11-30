from sklearn.metrics.pairwise import cosine_similarity
from scripts import *
from article import Article
import jsonpickle

def get_top_k_cosine_similarity_value(query,top_tk):
    results = dict()
    query = np.array([vectorize_query(query)])
    with open('backend\\article_vector.json') as article_vectors:
        articles = json.load(article_vectors)
        for (article_name,article_vector) in articles.items():
            results[article_name] = float(
                cosine_similarity(query, np.array([article_vector]))[0][0])
    result = [Article(title, score)
              for (title, score) in sorted_top_k(results,top_tk)]
    return str(jsonpickle.encode(result, unpicklable=False))
    
    

if __name__ == "__main__":
    query = ["capital",
    "urban_area.city",
    "company",
    "administrative_district.city",
    "district"]
    
    print(get_top_k_cosine_similarity_value(query,10))
