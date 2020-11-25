#!/usr/bin/env python
# coding: utf-8

# ### Web Scrapping App

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import requests


# In[2]:


executable_path = {"executable_path": "/usr/local/bin/chromedriver"} 
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:
def scrape():


    mars_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"


    # In[4]:


    browser.visit(mars_url)


    # In[13]:


    html = browser.html
    soup = bs(html, "html.parser")
    soup


    # In[16]:


    # mars_title = soup.find_all("div", class_="content_title")[1].text
    mars_title = soup.title.string
    mars_title


    # In[15]:


    # mars_paragraph = soup.find("div", class_="article_teaser_body")
    # mp = mars_paragraph[1].text
    mp = soup.p.string
    mp


    # In[ ]:





    # In[17]:


    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"


    # In[18]:


    browser.visit(jpl_url)

    #html = browser.html
    #soup = bs(html, "html.parser")


    # In[19]:


    browser.click_link_by_partial_text("FULL IMAGE")


    # In[20]:


    browser.click_link_by_partial_text("more info")


    # In[21]:


    html = browser.html
    soup = bs(html, "html.parser")


    # In[22]:


    image1 = soup.find_all("figure", class_="lede")[0].a["href"]
    image1


    # In[23]:


    jpl_image = "https://www.jpl.nasa.gov" + image1
    jpl_image


    # In[24]:


    ##Mars Facts


    # In[28]:


    Mars_facts = pd.read_html("https://space-facts.com/mars/")
    Mars_facts


    # In[30]:


    marsfactsdf = Mars_facts[0]
    marsfactsdf


    # In[31]:


    marsfactsdf.columns = ["descriptions","values"]
    marsfactsdf.set_index(['descriptions'])


    # In[32]:


    marsfacts_html = marsfactsdf.to_html(classes = 'table table-striped')


    # In[33]:


    #Scraping Hemisphere Images
    Hemisphere_URL = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


    # In[34]:


    #Getting the response using requests
    Response = requests.get(Hemisphere_URL)
    HemisphereSoup = bs(Response.text, "html.parser")
    # HemisphereSoup


    # In[35]:


    #Trying to locate item link
    item_link = HemisphereSoup.find_all(class_="itemLink product-item")
    item_link


    # In[36]:


    #Loop through item link and get each element
    element_list = []
    for item in item_link:
        url = "https://astrogeology.usgs.gov" + item.get ("href")

        element_list.append(url)
    element_list


    # In[37]:


    #Go to each URL and grab the title and image 
    titleurl = []
    for link in element_list:
        Response = requests.get(link)
        LinkSoup = bs(Response.text, "html.parser")
    #Find Samples
        image = LinkSoup.find("a", href=True,text="Sample")['href']
        title = LinkSoup.find(class_="title").text.strip().replace(" Enhanced", '')
        titleurl.append({"title": title, "img_url": image})
    titleurl
    # Creating Dictionary
    scrapedata = {
        "title": mars_title, 
        "paragraph": mp,
        "image":  jpl_image,
        "table":  marsfacts_html,
        "hemisphere_image": titleurl,

    }
# Return scrape data
    return scrapedata
    # In[ ]:





    # In[ ]:




