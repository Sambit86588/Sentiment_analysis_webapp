from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import re
import io
import urllib, base64
import matplotlib
import matplotlib.pyplot as plt

#constants
SENTIMENTS = ["Very Bad☹️","Bad🙁","Neutral😐","Good🙂","Very Good😃"]
TOKENIZER = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
MODEL = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

#calculating sentiment
def calculating(sample):
    #initiating model
    tokens = TOKENIZER.encode(sample, return_tensors="pt")
    result = MODEL(tokens)
    rated_result = int(torch.argmax(result.logits))
    
    #matching sentiment score with words
    for count, i in enumerate(SENTIMENTS):
        if rated_result == count:
            return SENTIMENTS[count]


   
