# Packages
import streamlit as st

import random

from MovRec import rec_movies , recorder

from mailbot import emailbot , recorder_email


import time


from PIL import Image


#page name and image
img = Image.open('bs.png')
st.beta_set_page_config(page_title="MovRec",page_icon=img,initial_sidebar_state="collapsed")


#Background Image
page_bg_img = '''
<style>
body {
background-image: url("https://previews.123rf.com/images/jakkapan/jakkapan1801/jakkapan180100003/92620273-abstract-dirty-or-aging-film-frame-dust-particle-and-dust-grain-texture-or-dirt-overlay-use-effect-f.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

#Title
title_html = """<div><p style="text-align:center; color:DarkOrange; font-size:45px"><b>🎻🎼💻📱🎥🎥📱💻🎼🎻Movie Recommendation Engine</b></p></div>"""
st.markdown(title_html, unsafe_allow_html = True)

#Search Box

liked_movie = st.text_input("")
button_clicked = st.button("Recommend")

#boder colour
color = ["red","orange","blue","Tomato","DodgerBlue","MediumSeaGreen"]
color = random.choice(color)

#Html for name card
end_html = '''<h3 align="right">Nikhil Narasimha</h3> 
              <h3 align="right">7799528666</h3>'''

if len(liked_movie) < 3:
    pass
elif (len(liked_movie) >= 3 and button_clicked) or len(liked_movie) >= 3 :
    
    movie_liked_edited, df = rec_movies(liked_movie)
    search_word_html = """</style><div><p style="text-align:left; color:Black; font-size:30px; font-family: monospace;"><i>Searched for movies like <b>"{movie_liked_edited}"</b></i></p></div>"""
    search_word_html = search_word_html.format(movie_liked_edited = movie_liked_edited.title())
    st.markdown(search_word_html, unsafe_allow_html = True)
    html = '''
        <div class="container" style="display: flex; border:2px solid {colour}; background-color: white;">
        <div style="width: 40%;" >
                <div>
                    <div style="width: 80%; ">
                        <img src="{img}" style = "display:block; margin:auto; width:80;">
                    </div>
                </div>
         </div>
         <div style="flex-grow: 1; ">
                <div >
                       <h1  margin: 0px 0px 5px; style="font-family:verdana">{movie_name}</h1>
                        <div >
                             <span><b>Genre :</b></span>
                              <span><a style="color:#000;">{genre}</a></span>
                        </div>
                 <div>
                         <b>Release Date : </b><span>{release_date}</span>
                 </div>
                <div >
                      <span><b>Cast :</b></span>
                       <a style="color:#000;">{cast}</a>
                </div>
                <div >
                       <div >
                            <span><b>Director :</b></span> <a style="color:#000;">{director}</a>
                       </div>
                       <div >
                            <span><b>Producer :</b></span> <a style="color:#000;">{producer}</a>
                       </div>
                </div>
        </div>
     </div>
    
     '''
    html1 = html.format(img = df["movie_Image"][1],movie_name = (df["movie_name"][1]).title(),genre = (df["genre"][1]).title(),release_date = df["release_date"][1], cast = (df["main_cast"][1]).title(),director = (df["director"][1]).title(),producer = df["producer"][1], colour= color )
    st.markdown(html1, unsafe_allow_html=True)
    st.title(" ")
    html2 = html.format(img = df["movie_Image"][2],movie_name = (df["movie_name"][2]).title(),genre = (df["genre"][2]).title(),release_date = df["release_date"][2], cast = (df["main_cast"][2]).title(),director = (df["director"][2]).title(),producer = df["producer"][2], colour= color )
    st.markdown(html2, unsafe_allow_html=True)
    st.title(" ")
    html3 = html.format(img = df["movie_Image"][3],movie_name = (df["movie_name"][3]).title(),genre = (df["genre"][3]).title(),release_date = df["release_date"][3], cast = (df["main_cast"][3]).title(),director = (df["director"][3]).title(),producer = df["producer"][3], colour= color )
    st.markdown(html3, unsafe_allow_html=True)
    st.title(" ")
    html4 = html.format(img = df["movie_Image"][4],movie_name = (df["movie_name"][4]).title(),genre = (df["genre"][4]).title(),release_date = df["release_date"][4], cast = (df["main_cast"][4]).title(),director = (df["director"][4]).title(),producer = df["producer"][4], colour= color )
    st.markdown(html4, unsafe_allow_html=True)
    st.title(" ")
    html5 = html.format(img = df["movie_Image"][5],movie_name = (df["movie_name"][5]).title(),genre = (df["genre"][5]).title(),release_date = df["release_date"][5], cast = (df["main_cast"][5]).title(),director = (df["director"][5]).title(),producer = df["producer"][5], colour= color )
    st.markdown(html5, unsafe_allow_html=True)
    st.title(" ")
    html6 = html.format(img = df["movie_Image"][6],movie_name = (df["movie_name"][6]).title(),genre = (df["genre"][6]).title(),release_date = df["release_date"][6], cast = (df["main_cast"][6]).title(),director = (df["director"][6]).title(),producer = df["producer"][6], colour= color )
    st.markdown(html6, unsafe_allow_html=True)
    st.title(" ")
    html7 = html.format(img = df["movie_Image"][7],movie_name = (df["movie_name"][7]).title(),genre = (df["genre"][7]).title(),release_date = df["release_date"][7], cast = (df["main_cast"][7]).title(),director = (df["director"][7]).title(),producer = df["producer"][7], colour= color )
    st.markdown(html7, unsafe_allow_html=True)
    st.title(" ")
    html8 = html.format(img = df["movie_Image"][8],movie_name = (df["movie_name"][8]).title(),genre = (df["genre"][8]).title(),release_date = df["release_date"][8], cast = (df["main_cast"][8]).title(),director = (df["director"][8]).title(),producer = df["producer"][8], colour= color )
    st.markdown(html8, unsafe_allow_html=True)
    st.title(" ")
    html9 = html.format(img = df["movie_Image"][9],movie_name = (df["movie_name"][9]).title(),genre = (df["genre"][9]).title(),release_date = df["release_date"][9], cast = (df["main_cast"][9]).title(),director = (df["director"][9]).title(),producer = df["producer"][9], colour= color )
    st.markdown(html9, unsafe_allow_html=True)
    st.title(" ")
    html10 = html.format(img = df["movie_Image"][10],movie_name = (df["movie_name"][10]).title(),genre = (df["genre"][10]).title(),release_date = df["release_date"][10], cast = (df["main_cast"][10]).title(),director = (df["director"][10]).title(),producer = df["producer"][10], colour= color )
    st.markdown(html10, unsafe_allow_html=True)
    st.title(" ")
    html11 = html.format(img = df["movie_Image"][11],movie_name = (df["movie_name"][11]).title(),genre = (df["genre"][11]).title(),release_date = df["release_date"][11], cast = (df["main_cast"][11]).title(),director = (df["director"][11]).title(),producer = df["producer"][11], colour= color )
    st.markdown(html11, unsafe_allow_html=True)
    st.title(" ")
    html12 = html.format(img = df["movie_Image"][12],movie_name = (df["movie_name"][12]).title(),genre = (df["genre"][12]).title(),release_date = df["release_date"][12], cast = (df["main_cast"][12]).title(),director = (df["director"][12]).title(),producer = df["producer"][12], colour= color )
    st.markdown(html12, unsafe_allow_html=True)
    st.title(" ")
    html13 = html.format(img = df["movie_Image"][13],movie_name = (df["movie_name"][13]).title(),genre = (df["genre"][13]).title(),release_date = df["release_date"][13], cast = (df["main_cast"][13]).title(),director = (df["director"][13]).title(),producer = df["producer"][13], colour= color )
    st.markdown(html13, unsafe_allow_html=True)
    st.title(" ")
    html14 = html.format(img = df["movie_Image"][14],movie_name = (df["movie_name"][14]).title(),genre = (df["genre"][14]).title(),release_date = df["release_date"][14], cast = (df["main_cast"][14]).title(),director = (df["director"][14]).title(),producer = df["producer"][14], colour= color )
    st.markdown(html14, unsafe_allow_html=True)
    st.title(" ")
    html15 = html.format(img = df["movie_Image"][15],movie_name = (df["movie_name"][15]).title(),genre = (df["genre"][15]).title(),release_date = df["release_date"][15], cast = (df["main_cast"][15]).title(),director = (df["director"][15]).title(),producer = df["producer"][15], colour= color )
    st.markdown(html15, unsafe_allow_html=True)
    st.title(" ")
    html16 = html.format(img = df["movie_Image"][16],movie_name = (df["movie_name"][16]).title(),genre = (df["genre"][16]).title(),release_date = df["release_date"][16], cast = (df["main_cast"][16]).title(),director = (df["director"][16]).title(),producer = df["producer"][16], colour= color )
    st.markdown(html16, unsafe_allow_html=True)
    st.title(" ")
    html17 = html.format(img = df["movie_Image"][17],movie_name = (df["movie_name"][17]).title(),genre = (df["genre"][17]).title(),release_date = df["release_date"][17], cast = (df["main_cast"][17]).title(),director = (df["director"][17]).title(),producer = df["producer"][17], colour= color )
    st.markdown(html17, unsafe_allow_html=True)
    st.title(" ")
    html18 = html.format(img = df["movie_Image"][18],movie_name = (df["movie_name"][18]).title(),genre = (df["genre"][18]).title(),release_date = df["release_date"][18], cast = (df["main_cast"][18]).title(),director = (df["director"][18]).title(),producer = df["producer"][18], colour= color )
    st.markdown(html18, unsafe_allow_html=True)
    st.title(" ")
    html19 = html.format(img = df["movie_Image"][19],movie_name = (df["movie_name"][19]).title(),genre = (df["genre"][19]).title(),release_date = df["release_date"][19], cast = (df["main_cast"][19]).title(),director = (df["director"][19]).title(),producer = df["producer"][19], colour= color )
    st.markdown(html19, unsafe_allow_html=True)
    st.title(" ")
    html20 = html.format(img = df["movie_Image"][20],movie_name = (df["movie_name"][20]).title(),genre = (df["genre"][20]).title(),release_date = df["release_date"][20], cast = (df["main_cast"][20]).title(),director = (df["director"][20]).title(),producer = df["producer"][20], colour= color )
    st.markdown(html20, unsafe_allow_html=True)
    st.title(" ")
    recorder(liked_movie,movie_liked_edited)
    #Email
    st.markdown("*You can drop your EmailID to get Top 30 Movies Similiar to your movie throught Email.")
    col1, col2 = st.beta_columns(2)
    with col2:
        my_expander = st.beta_expander('Drop your Email here')
        mail_id = my_expander.text_input("  ")
        email_submit = my_expander.button('Get Mail!📧')
        if (r'@' in mail_id and len(mail_id) > 15)or (email_submit and r'@' in mail_id and len(mail_id) > 15) :
            result = emailbot(movie_liked_edited,df,mail_id)
            recorder_email(mail_id)
            my_expander.write(result)
    st.markdown(end_html, unsafe_allow_html=True)






















