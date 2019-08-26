#!/usr/bin/env python
# coding: utf-8

# In[155]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[22]:

def scrape():
    #scrape mars site and put it into soup
    url = "https://mars.nasa.gov/news/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')


    # In[35]:


    #make news paragraph variable
    newspara = soup.find('div', class_="image_and_description_container").find('div', class_="rollover_description_inner").text.strip()



    # In[36]:


    #make news titel variable
    newstitle = soup.find('div', class_="content_title").find('a').text.strip()



    # In[114]:


    #scrape jpl.nasa.gov site for image URL
    url2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.text)


    # In[120]:


    #get url extension
    url_ext=soup2.find('a', class_="button fancybox")["data-fancybox-href"]

    #create base url
    base_url = "https://www.jpl.nasa.gov"

    #concatenated url
    img_url = base_url+url_ext



    # In[121]:


    #scrape twitter
    url3 = "https://twitter.com/MarsWxReport"
    response3 = requests.get(url3)
    soup3 = BeautifulSoup(response3.text)


    # In[154]:


    #clean up tweet to remove \'n'\
    tweet=soup3.find('div', class_="js-tweet-text-container").find('p',class_="tweet-text").text.replace('\n','')



    # In[159]:


    #scrape Mars Facts table
    #url4="https://space-facts.com/mars/"
    #tables = pd.read_html(url4)
    #df = tables[0]



    # In[164]:


    #put Mars Facts table into an HTML string
    #NOT WORKING - bson.errors.InvalidDocument: cannot encode object
    #df.to_html("marsfacts.html")
    #tablehtml = df.to_string


    # In[162]:


    #collect URLs for hemispheres
    #Note: It might be a little short-cutty to just manually input these URLs like this, and
    #I see that I could use Splinter to do this (like if there were 100s of URLs to do this to). 
    #Wasn't sure if this was necessary for the assignment
    #It is far more expedient in this case to just go to each page, hover over the URL, and right-click
    #copy link address

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
        {"title": "Cerberus Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
        {"title": "Schiaparelli Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif"},
        {"title": "Syrtis Major Hemisphere", "img_url": "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
    ]

    hemisphere_image_url_1 = "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"
    hemisphere_image_url_2 = "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"
    hemisphere_image_url_3 = "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"
    hemisphere_image_url_4 = "http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"

    # In[166]:


    all_scraped={
        "newspara": newspara,
        "newstitle": newstitle,
        "img_url": img_url,
        "tweet":tweet,
        #"tablehtml":tablehtml,
        "hemisphere_image_urls":hemisphere_image_urls,    
        "hemisphere_image_url_1":hemisphere_image_url_1,
        "hemisphere_image_url_2":hemisphere_image_url_2,
        "hemisphere_image_url_3":hemisphere_image_url_3,
        "hemisphere_image_url_4":hemisphere_image_url_4
    }


    return all_scraped




