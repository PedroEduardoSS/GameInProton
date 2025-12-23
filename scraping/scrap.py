import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
from typing import Tuple
from nicegui import ui
from google import genai

load_dotenv()

def search_games(game: str) -> Tuple:
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(f"https://www.protondb.com/search?q={game}")

    #results = driver.find_elements(by=By.TAG_NAME, value="a")
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find("div", class_="styled__Flex-sc-g24nyo-0 styled__Row-sc-g24nyo-4 GameLayout__GenericContainer-sc-bqe883-0 GameLayout__MobileUpContainer-sc-bqe883-1 gMlTmq dKXMgt yIWdu iTMDdw")
    a_elements = div.find_all("a")[1::2]

    game_names = [e.get_text() for e in a_elements]
    game_links = [f"https://www.protondb.com{e.get('href')}" for e in a_elements]
    game_list = tuple(zip(game_names, game_links))


    time.sleep(3)
    driver.quit()
    return game_list

def game_report():
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a few words"
    )
    print(response.text)