from scraper import BookScraper
from network import CreateNetwork

x = BookScraper()
x.get_transcript()

y = CreateNetwork()
y.create_df()
y.characters()