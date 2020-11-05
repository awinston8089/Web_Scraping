#

from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

executable_path = {"executable_path": "/usr/local/bin/chromedriver"} 
browser = Browser("chrome", **executable_path, headless=False)

#Going to browser to scrape news title,
mars_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

browser.visit(mars_url)

#
html = browser.html
soup = bs(html, "html.parser")

mars_title = soup.find_all("div", class_="content_title")[1].text
mars_title 

mars_title = soup.find_all("div", class_="content_title")[1].text
mars_title

###