from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import time

service = Service(ChromeDriverManager().install())
print(service)
driver = webdriver.Chrome(service=service)

driver.get("https://www.protondb.com/search?q=rdr2")

#results = driver.find_elements(by=By.TAG_NAME, value="a")
time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
div = soup.find("div", class_="styled__Flex-sc-g24nyo-0 styled__Row-sc-g24nyo-4 GameLayout__GenericContainer-sc-bqe883-0 GameLayout__MobileUpContainer-sc-bqe883-1 gMlTmq dKXMgt yIWdu iTMDdw")
a_elements = div.find_all("a")

print(a_elements)
time.sleep(6)
driver.quit()