import selenium as se
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--window-size=1024x768")
chrome_options.add_argument("--headless")

# Try if chrome driver is on path
try:
    driver = webdriver.Chrome(chrome_options = chrome_options)
except se.common.exceptions.WebDriverException:
    # Default install location at linux
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options = chrome_options)

def search(searchQuery):
	searchQuery = searchQuery.replace(' ','+')
	driver.get('http://www.google.com/search?q=' + searchQuery)
	answer = driver.execute_script("""return document.elementFromPoint(arguments[0],arguments[1],arguments[2]);""", 350, 230,230).text
	return answer