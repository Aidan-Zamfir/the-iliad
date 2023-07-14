from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class BookScraper:

    def __init__(self):
        self.driver = webdriver.Chrome()


    def get_transcript(self):
        """Get book transcript"""

        self.driver.get("https://greekmythology.fandom.com/wiki/The_lliad")
        page = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div')
        iliad = page.find_elements(By.TAG_NAME, 'p')

        with open("IliadTranscript.txt", "w") as f:
            for i in iliad[4:]:
                f.write(f"{i.text}\n")
