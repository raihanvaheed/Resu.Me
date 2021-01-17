# All Code together
import pandas as pd
import numpy as np
import itertools
from docx import Document
import docx
import os
from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity



 # CHANGE THE BRACKET VALUE TO RESUME INPUT FILE

def check_key_words(resume_file, Job):
    keywords_list = {'Software Developer': ['teamwork',
 'workflow',
 'microsoft',
 'ecommerce',
 'html5',
 'developer',
 'online',
 'tools',
 'corporate',
 'html']}
    keywords = keywords_list[Job]
    resume = getText(resume_file)
    corpus = resume.split()
    corpus = [x.lower() for x in corpus]
    corpus = [x.replace(',', '') for x in corpus]
    corpus = [x.replace('.', '') for x in corpus]
    key_words_new = [x.lower() for x in key_words]
    for word in key_words_new:
        if (word in corpus):
            print ("The resume used the word {} which is a keyword for resumes of this type".format(word))
        else:
            print("You did not use the word {} which is key for a software dev job".format(word))
            

