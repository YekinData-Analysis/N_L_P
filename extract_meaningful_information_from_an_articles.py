# -*- coding: utf-8 -*-
"""Extract Meaningful Information From an Articles.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K8oxMUTqZdtiVLVXneAsaspPgEqDYy9H
"""

from newspaper import Article
import nltk

nltk.download("punkt")

url = "https://medium.com/@noiretravel29/most-popular-markets-in-lagos-42763d1e1ded#:~:text=Located%20on%20Lagos%20Island%2C%20Balogun,busiest%20markets%20in%20West%20Africa."
dframe=Article(url)
dframe.download()
dframe.parse()

dframe.title

dframe.publish_date

dframe.nlp()

dframe.summary

dframe.keywords

