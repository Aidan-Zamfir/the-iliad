import matplotlib.pyplot as plt
from pathlib import Path
import networkx as nx
import pandas as pd
import numpy as np
import spacy

NER = spacy.load("en_core_web_sm")
#call main df 'iliad_dataframe'        <------------here

class CreateNetwork:

    def __init__(self):
        self.book = open("IliadTranscript.txt").read()
        self.doc = NER(self.book)


    def create_df(self):
        """Create dataframe with sentence and NER characters column"""

        sentence_entity_list = []
        self.entity_list = []

        for i in self.doc.sents:
            self.entity_list = [j.text for j in i.ents]
            sentence_entity_list.append({'sentence': i, 'character': self.entity_list})

        sentence_ent_df = pd.DataFrame(sentence_entity_list)
        self.sentence_dataframe = sentence_ent_df[sentence_ent_df['character'].map(len) > 0]


    def characters(self):
        """From df, get frequency of individual 'character' entities
        & organize in list by frequency order"""

        characters = self.sentence_dataframe['character'].value_counts().index.tolist()
        print(characters)

