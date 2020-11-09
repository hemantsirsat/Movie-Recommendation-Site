import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Recommend:
    
    def show_similar_movies(movie_user_likes):
        def get_title_from_index(index):
            return df[df.index == index]["title"].values[0]

        def get_imdb_from_index(index):
            try:
                return df[df.index == index]["vote_average"].values[0]
            except:
                i=1

        def get_index_from_title(title):
            try:
                return df[df.title == title]["index"].values[0]
            except:
                i=1

        df = pd.read_csv('movie_dataset.csv')

        features = ['keywords','cast','genres','director']

        def combine_features(row):
            return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']

        for feature in features:
            df[feature] = df[feature].fillna('')
            
        df["combined_features"] = df.apply(combine_features,axis=1)
        df.iloc[0].combined_features

        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df['combined_features'])
        cosine_sim= cosine_similarity(count_matrix)

        movie_index = get_index_from_title(movie_user_likes)
        similar_movies = list(enumerate(cosine_sim[movie_index]))
        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

        i=0
        result = []
        for element in sorted_similar_movies:
            result.append((get_title_from_index(element[0])))
            i=i+1
            if i>5:
                break
        if result !=[]:
            return [results for results in result] 
        else:
            return(["No Such Movie Found. Enter Name Starting with Capital Alphabet or Try Different Movie"])