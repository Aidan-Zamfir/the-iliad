from scraper import BookScraper
from network import CreateNetwork
import os

if os.path.isfile("IliadTranscript.txt"):
    pass
else:
    x = BookScraper()
    x.get_transcript()

y = CreateNetwork()
y.create_df()
y.characters()