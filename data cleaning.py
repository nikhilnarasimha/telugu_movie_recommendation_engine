# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:49:54 2020

@author: NIKHIL NARASIMHA
"""
import pandas as pd

import re

df = pd.read_csv("telugu_movies_data.csv")

df.columns
#Movie Name

df["movie_name"] = df["movie_name"].apply(lambda x: x.strip())
df["movie_name"] = df["movie_name"].apply(lambda x: x.lower())

#genre

df["genre"] = df["genre"].apply(lambda x: x.replace("['",''))
df["genre"] = df["genre"].apply(lambda x: x.replace("']",''))
df["genre"] = df["genre"].apply(lambda x: x.replace("'",''))
df["genre"] = df["genre"].apply(lambda x: x.replace("]",''))

def rempunc(gen):
    s = re.sub('([.,!?()])', r'\1', gen)
    s = re.sub('\s{2,}', ' ', s)
    s = re.sub(r',', "", s)
    return s.strip()


df["genre2"] = df["genre"].apply(lambda x: rempunc(x))
df["genre2"] = df["genre2"].apply(lambda x: x.lower())
df["genre2"].isnull().sum()


#release date
df["release_date"] = df["release_date"].apply(lambda x: x.strip())

year = re.compile(r'\d\d\d\d')
df["release_year"] = df["release_date"].apply(lambda x: year.search(x).group() )

#grade
def editgrade(x):
    res = re.sub(r'\|.*',"",x)
    return res
df["grade"].fillna("Action", inplace = True) 
df["grade"] = df["grade"].apply(lambda x: x.strip())

df["grade"] = df["grade"].apply(lambda x: editgrade(x))
df["grade"] = df["grade"].apply(lambda x: x.replace("\n"," "))

glist = ["U","A","U/A"]
 
def wordre(word):
    try:
        w = [w for w in word.split() if w in glist][0]
        return w
    except:
        pass
        
df["grade"] = df["grade"].apply(lambda x: wordre(x))

df[df["grade"].isnull() == True]

#main cast
df.columns
df["main_cast"][8]

df["main_cast"].isnull().sum()
df["main_cast"] = df["main_cast"].apply(lambda x: x.replace("['",''))
df["main_cast"] = df["main_cast"].apply(lambda x: x.replace("']",''))
df["main_cast"] = df["main_cast"].apply(lambda x: x.replace("'",''))
df["main_cast2"] = df["main_cast"]


def rempunc(gen):
    s = re.sub('([.,!?()])', r'\1', gen)
    s = re.sub('\s{2,}', ' ', s)
    s = re.sub(r',', "", s)
    return s.strip()

def joinwords(text):
    s = re.sub('([.,!?()])', r' \1 ', text)
    sen = re.sub('\s{2,}', ' ', s)
    return sen

df["main_cast"] = df["main_cast"].apply(lambda x: rempunc(x))
df["main_cast"] = df["main_cast"].apply(lambda x: x.lower())


df["main_cast2"] = df["main_cast2"].apply( lambda x: x.replace(" ",""))
df["main_cast2"] = df["main_cast2"].apply( lambda x: joinwords(x))
df["main_cast2"] = df["main_cast2"].apply(lambda x: rempunc(x))
df["main_cast2"] = df["main_cast2"].apply(lambda x: x.lower())


#director
df.columns

df["director"].isnull().sum()
df["director"][8]
df["director"] = df["director"].apply(lambda x: x.strip())
df["director"] = df["director"].apply(lambda x: x.lower())

df["director2"] = df["director"]
df["director2"] = df["director2"].apply( lambda x: x.replace(" ",""))
df["director2"] = df["director2"].apply( lambda x: joinwords(x))
df["director2"] = df["director2"].apply(lambda x: rempunc(x))
df["director2"] = df["director2"].apply(lambda x: x.lower())


#critics_rating
df["critics_rating"].isnull().sum()
df["critics_rating"].fillna("che",inplace = True)
df["critics_rating"][9]
df["critics_rating"] = df["critics_rating"].apply(lambda x: x.strip())

def recr(x):
    s = re.sub(r'\/.*',"",x)
    return s

df["critics_rating"] = df["critics_rating"].apply(lambda x: recr(x))

#audience_rating
df["audience_rating"].isnull().sum()
df["audience_rating"].fillna("che",inplace = True)
df["audience_rating"][9]
df["audience_rating"] = df["audience_rating"].apply(lambda x: x.strip())

def recr(x):
    s = re.sub(r'\/.*',"",x)
    return s

df["audience_rating"] = df["audience_rating"].apply(lambda x: recr(x))

#cast
df["cast"].isnull().sum()

df["cast"] = df["cast"].apply(lambda x: x.replace("['",''))
df["cast"] = df["cast"].apply(lambda x: x.replace("']",''))
df["cast"] = df["cast"].apply(lambda x: x.replace("]",''))
df["cast"] = df["cast"].apply(lambda x: x.replace("'",''))

df["cast2"] = df["cast"]
def rempunc(gen):
    s = re.sub('([.,!?()])', r'\1', gen)
    s = re.sub('\s{2,}', ' ', s)
    s = re.sub(r',', "", s)
    return s.strip()

df["cast"] = df["cast"].apply(lambda x: rempunc(x))
df["cast"] = df["cast"].apply(lambda x: x.lower())


df["cast2"][9]
df["cast2"] = df["cast2"].apply( lambda x: x.replace(" ",""))
df["cast2"] = df["cast2"].apply( lambda x: joinwords(x))
df["cast2"] = df["cast2"].apply(lambda x: rempunc(x))
df["cast2"] = df["cast2"].apply(lambda x: x.lower())

#crew
df["crew"].isnull().sum()

df["crew"] = df["crew"].apply(lambda x: x.replace("['",''))
df["crew"] = df["crew"].apply(lambda x: x.replace("']",''))
df["crew"] = df["crew"].apply(lambda x: x.replace("'",''))

df["crew2"] = df["crew"]

def rempunc(gen):
    s = re.sub('([.,!?()])', r'\1', gen)
    s = re.sub('\s{2,}', ' ', s)
    s = re.sub(r',', "", s)
    return s.strip()


df["crew"] = df["crew"].apply(lambda x: rempunc(x))
df["crew"] = df["crew"].apply(lambda x: x.lower())

df["crew2"][9]
df["crew2"] = df["crew2"].apply( lambda x: x.replace(" ",""))
df["crew2"] = df["crew2"].apply( lambda x: joinwords(x))
df["crew2"] = df["crew2"].apply(lambda x: rempunc(x))
df["crew2"] = df["crew2"].apply(lambda x: x.lower())

#crew_roles
df["crew_roles"].isnull().sum()
df["crew_roles"] = df["crew_roles"].apply(lambda x: x.replace("['",''))
df["crew_roles"] = df["crew_roles"].apply(lambda x: x.replace("']",''))
df["crew_roles"] = df["crew_roles"].apply(lambda x: x.replace("'",''))
df["crew_roles"][156]


df["crew_roles"] = df["crew_roles"].apply(lambda x: x[x.find("Director"):])

def rempunc(gen):
    s = re.sub('([.,!?()])', r'\1', gen)
    s = re.sub('\s{2,}', ' ', s)
    s = re.sub(r',', "", s)
    return s.strip()

df["crew_roles"] = df["crew_roles"].apply(lambda x: rempunc(x))

#stroy
df.columns
df["story"][66]
df["story"].isnull().sum()
df["story"] = df["story"].apply(lambda x: x.strip())
df["story"] = df["story"].apply(lambda x: x[:x.find("**Note:")].strip())
 

def keywordsexc(text):   
    import nltk
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens ]
    sen = ' '.join(words)
    import re
    s = re.sub('([.,!?()])', r' \1 ', sen)
    sen = re.sub('\s{2,}', ' ', s)
    tokens = word_tokenize(sen)
    words = [word for word in tokens if word.isalpha()]
    sen = ' '.join(words)
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    sen = re.sub(r'\b\w{1,2}\b', '', sen)
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(sen)
    words = [word for word in tokens if not word in stop_words]
    sen = ' '.join(words)
    from nltk.stem import PorterStemmer
    ps =PorterStemmer()
    tokens = word_tokenize(sen)
    words = [ps.stem(word) for word in tokens ]
    sen = ' '.join(words)
    return sen

text = df["story"][9]
text



df["story_brief"] = df["story"].apply(lambda x: keywordsexc(x))


def keywordsexc_withnouns(text):   
    import nltk
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens ]
    sen = ' '.join(words)
    import re
    s = re.sub('([.,!?()])', r' \1 ', sen)
    sen = re.sub('\s{2,}', ' ', s)
    tokens = word_tokenize(sen)
    words = [word for word in tokens if word.isalpha()]
    sen = ' '.join(words)
    from nltk.corpus import stopwords
    stop_words = stopwords.words('english')
    sen = re.sub(r'\b\w{1,2}\b', '', sen)
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(sen)
    words = [word for word in tokens if not word in stop_words]
    sen = ' '.join(words)
    return sen


df["story_brief_nouns"] = df["story"].apply(lambda x: keywordsexc_withnouns(x))

def keywordsexc_punc(text):   
    import nltk
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(text)
    words = [word.lower() for word in tokens ]
    sen = ' '.join(words)
    import re
    s = re.sub('([.,!?()])', r' \1 ', sen)
    sen = re.sub('\s{2,}', ' ', s)
    tokens = word_tokenize(sen)
    words = [word for word in tokens if word.isalpha()]
    sen = ' '.join(words)
    return sen


df["story_brief_punc"] = df["story"].apply(lambda x: keywordsexc_punc(x))

df["clen"] = df["story"].apply(lambda x: len(x))


df.to_csv("telugu_movies_cleaned.csv")


