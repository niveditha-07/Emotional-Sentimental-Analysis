from urllib import response
from http import client
import streamlit as st
import boto3
st.title("Sentimental Analysis")
#st.text("Enter text")
text=st.text_input("Enter text")
if st.button("Predict"):
    client=boto3.client('comprehend')
    response=client.detect_sentiment(
        Text=text,
        LanguageCode='en'
    )
    #st.write(response)

    if(response['Sentiment']=='POSITIVE'):
        st.success("Positive Statement")
    elif(response['Sentiment']=='NEGATIVE'):
        st.error("Negative statement")
    elif(response['Sentiment']=="NEUTRAL"):
        st.warning("Neutral")
    else:
        st.write("Mixed Statement")
