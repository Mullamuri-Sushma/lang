import streamlit as st 
import dotenv
import langchain

from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

import zipfile
import os
os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")

st.set_page_config(page_title="AI website creation",page_icon="😁")

st.title("AI AUTOMATION WEBSITE CREATION")

prompt=st.text_area("write here about your website")

if st.button("generate"):
    message=[("system","""you are a expert in web development mainly in frontend 
    so creative a professional way of html,css,javaScript code for creating a frontend based prompt
    The output should be in the below format:
    --html--
    [html code]
    --html--

    --css--
    [css code]
    --css--

    --js--
    [js code]
    --js-- """)]

    message.append(("user",prompt))
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

    response=model.invoke(message)

    #with open("file.txt","w") as file:
        #file.write(response.content)

    with open("index.html","w") as file:
        file.write(response.content.split("--html--")[1])

    with open("style.css","w") as file:
        file.write(response.content.split("--css--")[1])

    with open("script.js","w") as file:
        file.write(response.content.split("--js--")[1])

    with zipfile.ZipFile("website.zip","w") as zip:
        zip.write("index.html")
        zip.write("style.css")
        zip.write("script.js")

    st.download_button("Click to Download",data=open("website.zip","rb"),file_name="website.zip")
    st.write("success")