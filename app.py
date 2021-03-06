import streamlit as st
import re
from afinn import Afinn
af= Afinn(language='en', emoticons=False, word_boundary=True)

def text_cleaner (text):
    cleaned= re.sub('[^a-zA-Z]', " ", text) 
    cleaned= cleaned.lower()
    cleaned = cleaned.split()
    cleaned= ' '.join(cleaned)
    return cleaned

def score_calc(text):
    lst= text.split()
    sco=0
    for i in range(len(lst)):
        if lst[i-1]=="not":
            score = af.score(lst[i])*(-1)
        else:
            score =af.score(lst[i])
        sco += score
    return sco


st.header("Welocme to Review Analyzer of washing machine, We’re so happy you’re here!")


col1, col2, col3 = st.columns([1,1,1])
with col2:
    st.image("Was.png", width=200)


st.write("The concept is simple: You just enter the review and we will let you know the sentiment behind it, which will help you to Grow, Survive & Thrive")
input_review = st.text_input("Enter review here")
if st.button("Predict"):
    st.subheader("The Review Entered is")
    st.write (input_review)
    try:
        clean_rev = text_cleaner(input_review)
        sent_score = score_calc(clean_rev)
        if sent_score < 0:
            st.image("sad.png",width=50) 
            st.subheader("Sadly, its Negative Review!")
            st.subheader("There is scope for improvement")
        elif sent_score > 0:
            st.image("happy.png", width=70) 
            st.subheader("Hey, its Positive Review !!!")
            st.subheader("Great, Keep it up")
        else:
            st.image("mix.jpg", width=70) 
            st.subheader("Hey, Its Mixed Review")
            
    except:
        pass            

