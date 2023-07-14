from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import os

class CharacterScraper:

    def __init__(self):
        self.driver = webdriver.Chrome()


    def get_characters(self):
        """Scrape Homeric character names from wiki"""

        self.driver.get("https://en.wikipedia.org/wiki/List_of_Homeric_characters")
        page = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]')
        character_page = page.find_elements(By.CSS_SELECTOR, 'a')

        characters = [re.findall('[A-Z][^A-Z]*',i.text) for i in character_page]
        temp_char_list = []

        for i in characters:
            if i not in temp_char_list:
                temp_char_list.append(i)

        character_list = filter(None, temp_char_list)

        #have to manually delete a few entries (eg: 'the', 'soruce', etc)
        with open("HomericCharacters.txt", "w") as f:
            for i in list(character_list):
                    f.write(f"{i[0]}\n")