# To make easy the picking of article features
# This object represent an article
# one article has a title and a similarity score
# we use this when computing Cosine Similarity
class Article:
    def __init__(self, title, score):
        self.title = title
        self.score = score
