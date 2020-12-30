# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:45:43 2020

@author: NIKHIL NARASIMHA
"""
import pandas as pd
from fuzzywuzzy import process
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import time
import psycopg2


df = pd.read_csv("telugu_movies_cleaned.csv")

#recoder
def recorder(movie_liked,movie_name_given):
    try:
        localtime = time.asctime( time.localtime(time.time()))
        conn = psycopg2.connect(database = "d4p1j3ph7ovdpj", user = "ncanedrmvoiwrt",
                            password = "b57d5188229f2a87e436a3185fb69631b1c0d479ce8df57a16d64a4c1d101213", host = "ec2-23-20-205-19.compute-1.amazonaws.com", port = "5432",connect_timeout=5)
        mycursor = conn.cursor()
    
        sql = "INSERT INTO record_moverc (movie_name_given,movie_name_corrected,time)VALUES (%s, %s, %s)"
        val = (movie_liked,movie_name_given,localtime)
        mycursor.execute(sql, val)
        conn.commit()
        conn.close()
    except:
        print("recording Failed")
        pass

def get_title_from_index(index):
	return df[df.index == index]["movie_name"].values[0]

def get_index_from_title(title):
	return df[df.movie_name == title].index.values[0]

def combine_features(row):
    return row["story_brief"] +" "+ row["genre2"]+" "+ row["main_cast2"] +" "+  row["director2"] + " "+ row["crew2"]

df["combined_features"] = df.apply(combine_features, axis = 1)


#Algorthim
tfidfvec = TfidfVectorizer(ngram_range = (1,2))
tfidf_movie_matrix = tfidfvec.fit_transform(df["combined_features"])

cosine_sim = cosine_similarity(tfidf_movie_matrix)


#movies_list
movies = df["movie_name"].to_list()


#Function fo recommdation
def rec_movies(movie_liked):
    movie_liked = movie_liked.strip()
    movie_liked = movie_liked.lower()
    movie_name_given = process.extract(movie_liked, movies)[0][0]
    movie_index = get_index_from_title(movie_name_given)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_movies = sorted(similar_movies, key = lambda x: x[1], reverse = True)
    recommeded_movies = [get_title_from_index(x[0]) for x in sorted_movies]
    recommeded_movies_50 = pd.DataFrame(recommeded_movies[0:50], columns = ["movie_name"])
    recommeded_movies_50_Info = pd.merge(recommeded_movies_50,df.loc[df["movie_name"].isin(recommeded_movies_50["movie_name"])], on = "movie_name" )    
    return movie_name_given, recommeded_movies_50_Info












