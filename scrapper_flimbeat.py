# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:00:26 2020

@author: NIKHIL NARASIMHA
"""
import uuid

import pandas as pd

import requests

from bs4 import BeautifulSoup

base_url = "https://www.filmibeat.com/telugu/movies/december-.html"

months = ["january","february","march","april","may","june","july","august","september","october","november","december"]

years = ["2013","2014","2015","2016","2017","2017","2017","2018","2019","2020"]

urls = []
for y in years:
    for m in months:
        u = "https://www.filmibeat.com/telugu/movies/{m}-{y}.html"
        u = u.format(m = m , y= y)
        urls.append(u)
        
URL_S_df = pd.DataFrame(urls)  

URL_S_df = URL_S_df.drop(119)    
#Movie URls
movie_urls = []


for u in URL_S_df[0]:
    res = requests.get(u)
    c = res.content   
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class" : "movie-name"})
    for i in all:
        movie_url = i.findAll('a')
        for url in movie_url:
            m_url = url.get('href')
            movie_urls.append(m_url)


str(uuid.uuid1())

#Information scrapping

data = []

for url in movie_urls:
    d = {}
    try:          
        d["uid"] = str(uuid.uuid1())
        d["url"] = url
        res = requests.get(url, timeout=15)
        c = res.content
        soup = BeautifulSoup(c, "html.parser")
        all = soup.find_all("div", {"class" : "overview-movie-details"})
        for i in all:
            d["movie_name"] = i.find_all("h1")[0].text
        all = soup.find_all("div", {"class" : "overview-movie-img"})
        for i in all:
            image = i.findAll('img')
            for img in image:
                d["movie_Image"] = img.get('src')
    
        genre = []
        all = soup.find_all("div", {"class" : "ov-mov-timing"})
        for i in all:
            g2 = i.find_all("a")
            for g in g2:
                genre.append(g.text)
        
        d["genre"] = genre
        all = soup.find_all("div", {"class" : "ov-mov-rel-dat"})
        for i in all:
            d["release_date"] = (i.find_all("span")[0].text)
        all = soup.find_all("div", {"class" : "ov-mov-timing"})
        for i in all:
            d["grade"] = i.text
        Cast = []
        all = soup.find_all("div", {"class" : "ov-mov-cast"})
        for i in all:
            c2 = (i.find_all("a"))
            for c in c2:
                Cast.append(c.text)
        d["main_cast"] = Cast
        all = soup.find_all("div", {"class" : "ov-mov-banner"})
        for i in all:
            d["director"] = (i.find_all("a")[0].text)
        all = soup.find_all("div", {"class" : "rating-block"})
        for i in all:
            rat = i.find_all("div",{"class" : "rating-num critics"})
            for rating in rat:
                d["critics_rating"] = (rating.text)
        all = soup.find_all("div", {"class" : "ov-like-block"})
        for i in all:
            rat = i.find_all("div",{"class" : "rating-num critics"})
            for rating in rat:
                d["audience_rating"] = (rating.text)
        all = soup.find_all("div", {"class" : "cast-name"})
        l = []
        for i in all:
            l.append(i.text)
        Cast = [item.strip() for item in l]
        d["cast"] = Cast
        all = soup.find_all("div", {"class" : "crew-name"})
        l = []
        for i in all:
            l.append(i.text)
        Crew = [item.strip() for item in l]
        d["crew"] = Crew
        all = soup.find_all("div", {"class" : "crew-name"})
        producer = all[1].text
        producer = producer.strip()
        d["producer"] = producer
        all = soup.find_all("div", {"class" : "char-name"})
        l = []
        for i in all:
            l.append(i.text)
        Crew_roles = [item.strip() for item in l]
        d["crew_roles"] = Crew_roles
        all = soup.find_all("div", {"class" : "critics-info"})
        l = []
        for i in all:
            l.append(i.text)
        critics = [item.strip() for item in l]
        d["critics_review"] = critics
        
        url = url.replace(".html", "")
        story_url = "/story.html"
        url = url + story_url
        res = requests.get(url)
        
        c = res.content
        
        soup = BeautifulSoup(c, "html.parser")
        
        all = soup.find_all("div", {"class" : "mv-story"})
        for i in all:
            d["story"] = (i.text)
        
        data.append(d)
    except:
        d["url"] = url
        d["movie_name"] = "error"
        data.append(d)
        
    
df = pd.DataFrame(data)
    
    
    
    
#analysis    

url = "https://www.filmibeat.com/telugu/movies/uma-maheswara-ugra-roopasya.html"

res = requests.get(url)

c = res.content

soup = BeautifulSoup(c, "html.parser")
soup
#movie name
all = soup.find_all("div", {"class" : "overview-movie-details"})
for i in all:
    print(i.find_all("h1")[0].text)

#movie image
all = soup.find_all("div", {"class" : "overview-movie-img"})
for i in all:
    image = i.findAll('img')
    for img in image:
        print(img.get('src'))

#movie grade
all = soup.find_all("div", {"class" : "ov-mov-timing"})
for i in all:
    print(i.text)




#genre
genre = []
all = soup.find_all("div", {"class" : "ov-mov-timing"})
for i in all:
    g2 = i.find_all("a")
    for g in g2:
        genre.append(g.text)

    

#release date
all = soup.find_all("div", {"class" : "ov-mov-rel-dat"})
for i in all:
    print(i.find_all("span")[0].text)

#Cast
Cast = []
all = soup.find_all("div", {"class" : "ov-mov-cast"})
for i in all:
    c2 = (i.find_all("a"))
    for c in c2:
        Cast.append(c.text)
        
    

#Director
all = soup.find_all("div", {"class" : "ov-mov-banner"})
for i in all:
    print(i.find_all("a")[0].text)



#Critics rating
all = soup.find_all("div", {"class" : "rating-block"})
for i in all:
    rat = i.find_all("div",{"class" : "rating-num critics"})
    for rating in rat:
        print(rating.text)

#User rating
all = soup.find_all("div", {"class" : "ov-like-block"})
for i in all:
    rat = i.find_all("div",{"class" : "rating-num critics"})
    for rating in rat:
        print(rating.text)
  

#OverAll- Cast
all = soup.find_all("div", {"class" : "cast-name"})
l = []
for i in all:
    l.append(i.text)
Cast = [item.strip() for item in l]
print(Cast)


#OverAll- Crew
all = soup.find_all("div", {"class" : "crew-name"})
l = []
for i in all:
    l.append(i.text)
Crew = [item.strip() for item in l]
print(Crew)


#Director
all = soup.find_all("div", {"class" : "crew-name"})
director = all[0].text
director = director.strip()
director

#Producer
all = soup.find_all("div", {"class" : "crew-name"})
director = all[1].text
producer = director.strip()
producer



#OverAll- Crew - roles
all = soup.find_all("div", {"class" : "char-name"})
l = []
for i in all:
    l.append(i.text)
Crew = [item.strip() for item in l]
print(Crew)


#crictics review
all = soup.find_all("div", {"class" : "critics-info"})
l = []
for i in all:
    l.append(i.text)
critics = [item.strip() for item in l]
print(critics)


#Story 
url = url.replace(".html", "")
story_url = "/story.html"
url = url + story_url
res = requests.get(url)

c = res.content

soup = BeautifulSoup(c, "html.parser")

all = soup.find_all("div", {"class" : "mv-story"})
for i in all:
    print(i.text)



df.to_csv("telugu_movies_data.csv", index = False)


df = df[df["movie_name"] != "error"]



#Fix error URL's

data1 = []

for url in rerun["url"]:
    d = {}       
    d["uid"] = str(uuid.uuid1())
    d["url"] = url
    res = requests.get(url, timeout=60)
    c = res.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class" : "overview-movie-details"})
    for i in all:
        d["movie_name"] = i.find_all("h1")[0].text
    all = soup.find_all("div", {"class" : "overview-movie-img"})
    for i in all:
        image = i.findAll('img')
        for img in image:
            d["movie_Image"] = img.get('src')

    genre = []
    all = soup.find_all("div", {"class" : "ov-mov-timing"})
    for i in all:
        g2 = i.find_all("a")
        for g in g2:
            genre.append(g.text)
    
    d["genre"] = genre
    all = soup.find_all("div", {"class" : "ov-mov-rel-dat"})
    for i in all:
        d["release_date"] = (i.find_all("span")[0].text)
    Cast = []
    all = soup.find_all("div", {"class" : "ov-mov-cast"})
    for i in all:
        c2 = (i.find_all("a"))
        for c in c2:
            Cast.append(c.text)
    d["main_cast"] = Cast
    all = soup.find_all("div", {"class" : "ov-mov-banner"})
    for i in all:
        d["director"] = (i.find_all("a")[0].text)
    all = soup.find_all("div", {"class" : "rating-block"})
    for i in all:
        rat = i.find_all("div",{"class" : "rating-num critics"})
        for rating in rat:
            d["critics_rating"] = (rating.text)
    all = soup.find_all("div", {"class" : "ov-like-block"})
    for i in all:
        rat = i.find_all("div",{"class" : "rating-num critics"})
        for rating in rat:
            d["audience_rating"] = (rating.text)
    all = soup.find_all("div", {"class" : "cast-name"})
    l = []
    for i in all:
        l.append(i.text)
    Cast = [item.strip() for item in l]
    d["cast"] = Cast
    all = soup.find_all("div", {"class" : "crew-name"})
    l = []
    for i in all:
        l.append(i.text)
    Crew = [item.strip() for item in l]
    d["crew"] = Crew
    try:
        all = soup.find_all("div", {"class" : "crew-name"})
        producer = all[1].text
        producer = producer.strip()
        d["producer"] = producer
    except:
        pass
    all = soup.find_all("div", {"class" : "char-name"})
    l = []
    for i in all:
        l.append(i.text)
    Crew_roles = [item.strip() for item in l]
    d["crew_roles"] = Crew_roles
    all = soup.find_all("div", {"class" : "critics-info"})
    l = []
    for i in all:
        l.append(i.text)
    critics = [item.strip() for item in l]
    d["critics_review"] = critics
    
    url = url.replace(".html", "")
    story_url = "/story.html"
    url = url + story_url
    res = requests.get(url)
    
    c = res.content
    
    soup = BeautifulSoup(c, "html.parser")
    
    all = soup.find_all("div", {"class" : "mv-story"})
    for i in all:
        d["story"] = (i.text)
    
    data1.append(d)



dff = pd.DataFrame(data1)

df = df.append(dff)



















