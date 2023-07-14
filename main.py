from character_scraper import CharacterScraper
from book_scraper import BookScraper
from network import CreateNetwork
import os

def book():
    if os.path.isfile("text_files/IliadTranscript.txt"):
        pass
    else:
        book = BookScraper()

def characters():
    if os.path.isfile("text_files/HomericCharacters.txt"):
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

