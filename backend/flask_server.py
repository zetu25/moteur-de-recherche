from flask import Flask, jsonify, request
from cosine_similarity import *
from semantic_path_length import *
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/cosine-similarity', methods=['POST'])
def get_cosine_similarity():
    entities = request.json['entities']
    return get_top_k_cosine_similarity_value(entities, 10)


@app.route('/semantic-path-length', methods=['POST'])
def get_semantic_path_length():
    entities = request.json['entities']
    print(entities)
    semantic_path_dictionnary = getPathLengthSimilarity(entities)
    return semantic_path_dictionnary
     

if __name__ == '__main__':
    app.run()
