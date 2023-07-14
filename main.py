from scraper import BookScraper
from network import CreateNetwork
from char_scraper import CharacterScraper
import os

# if os.path.isfile("IliadTranscript.txt"):
#     pass
# else:
#     x = BookScraper()
#     x.get_transcript()
# if os.path.isfile("HomericCharacters.txt"):
#     pass
# else:
#     z = CharacterScraper()
#     z.get_characters()

y = CreateNetwork()
y.create_df()
y.characters()