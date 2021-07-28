from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://es.wikipedia.org/wiki/Will_Smith")

search = driver.find_element_by_name("firstHeading")