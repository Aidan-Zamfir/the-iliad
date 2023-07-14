import matplotlib.pyplot as plt
from pathlib import Path
import networkx as nx
from pyvis.network import Network
import community as community_louvain
import pandas as pd
import numpy as np
import spacy

NER = spacy.load("en_core_web_sm")

class CreateNetwork:

    def __init__(self):
        self.book = open("text_files/IliadTranscript.txt").read()
        self.doc = NER(self.book)
        self.window_size = 5
        self.run()

    def create_df(self):
        """Create dataframe with sentence and NER characters column"""

        with open("text_files/HomericCharacters.txt") as f:
            characters = f.read()

        sentence_entity_list = []
        self.entity_list = []

        for i in self.doc.sents:
            self.entity_list = [j.text for j in i.ents]
            sentence_entity_list.append({'sentence': i, 'character': self.entity_list})

        sentence_ent_df = pd.DataFrame(sentence_entity_list)


        sentence_ent_df['character'] = sentence_ent_df['character'].apply(lambda x: self.filter_names(x, characters))
        self.sentence_dataframe = sentence_ent_df[sentence_ent_df['character'].map(len) > 0]


    def filter_names(self, ent_list, chars):
        """Filter out non 'main character' entities.
        Called in self.create_df()"""

        return [i for i in ent_list if i in chars]


    def network(self):
        """Create relationship df"""

        self.relationships = []

        for i in range(self.sentence_dataframe.index[-1]):
            end_i = min(i+5, self.sentence_dataframe.index[-1])
            character_names = sum((self.sentence_dataframe.loc[i: end_i].character), [])

            self.unique_character = [character_names[i] for i in range(len(character_names))
                                    if (i == 0) or character_names[i] != character_names[i - 1]]

            if len(self.unique_character) > 1:
                for idx, a in enumerate(self.unique_character[:-1]):
                    b = self.unique_character[idx + 1]
                    self.relationships.append({'source': a, 'target': b, })

        self.iliad_dataframe =  pd.DataFrame(self.relationships)
        self.edge_weight()


    def edge_weight(self):
        """Remove duplicate relationships & create
        edge weight (relationship) between characters in df"""

        self.iliad_dataframe['value'] = 1
        self.iliad_dataframe = self.iliad_dataframe.groupby(['source', 'target'], sort=False, as_index=False).sum()


    def network_graph(self):
        """Create a network from df based on degree centrality"""

        net = Network(notebook=True, width='1000px', height='700px', bgcolor='#222222', font_color='white')
        net.repulsion()
        G = nx.from_pandas_edgelist(self.iliad_dataframe, source='source',
                                         target='target', edge_attr='value', create_using=nx.Graph())


        node_degree = dict(G.degree)
        nx.set_node_attributes(G, node_degree, 'size')

        net.from_nx(G)
        net.show('iliad.html')


    def community_network(self):
        """Create a community detection network
        & visualisation graph"""

        net = Network(notebook=True, width='1000px', height='700px', bgcolor='#222222', font_color='white')
        net.repulsion()
        G = nx.from_pandas_edgelist(self.iliad_dataframe, source='source',
                                    target='target', edge_attr='value', create_using=nx.Graph())

        communities = community_louvain.best_partition(G)
        nx.set_node_attributes(G, communities, 'group')

        net.from_nx(G)
        net.show("iliad_communities.html")

    def run(self):
        self.create_df()
        self.network()
        self.network_graph()
        self.community_network()
