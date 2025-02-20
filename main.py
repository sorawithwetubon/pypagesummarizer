#PyPageSummarizer - A Python library to summarize the main content of a webpage using Google T5 AI model.
#Author: Sorawith Wetubon
#License: MIT License
#Version: prerelease_v0.5.0

import requests #pip install requests - Fetch HTTP page content from a URL.
import trafilatura #pip install trafilatura - Extract main content from a webpage.
from transformers import pipeline #pip install transformers - Hugging Face Models for NLP tasks. & Pipeline for summarization task.
#pip install torch - PyTorch for Transformers.

summarizer = pipeline("summarization", model="t5-small") # Load the T5 model for summarization task.

def maincontent(url): # Function to extract the main content from a webpage.
    response = requests.get(url)
    text = trafilatura.extract(response.text)
    return text

def summarize(url,maxlength,minlength): # Function to summarize the main content extracted from a webpage.
    response = requests.get(url)
    text = trafilatura.extract(response.text)
    if len(text) < maxlength:
        maxlength = len(text) # If the length of the main content is less than the maximum length, set the maximum length to the length of the main content.
    summary = summarizer(text, max_length=maxlength, min_length=minlength, do_sample=False)
    return summary[0]['summary_text']

print(summarize("https://edition.cnn.com/2025/02/19/economy/trump-inflation-is-back/index.html",100,30))