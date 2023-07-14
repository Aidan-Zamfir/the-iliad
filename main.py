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
    data = CreateNetwork()


def main():
    book()
    characters()
    network()


if __name__ == '__main__':
    main()

