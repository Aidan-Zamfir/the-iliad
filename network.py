import matplotlib.pyplot as plt
from pathlib import Path
import networkx as nx
import pandas as pd
import spacy
import os

NER = spacy.load("en_core_web_sm")
class CreateNetwork:

    def __init__(self):
        pass

    def read_book(self):
        book = open("IliadTranscript.txt").read()
        self.doc = NER(book)
        print(self.doc)

    def create_df(self):
        pass