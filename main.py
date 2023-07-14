from book_scraper import BookScraper
from network import CreateNetwork
from character_scraper import CharacterScraper
import os

def book():
    if os.path.isfile("IliadTranscript.txt"):
        pass
    else:
        book = BookScraper()

def characters():
    if os.path.isfile("HomericCharacters.txt"):
        pass
    else:
        characters = CharacterScraper()

def network():
    y = CreateNetwork()
    y.create_df()

def main():
    book()
    characters()


if __name__ == '__main__':
    main()