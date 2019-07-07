from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import pandas as pd
from flask_pymongo import PyMongo

def scrape_info():
    #NASA Mars News
    nurl = 'https://mars.nasa.gov/news'
    nresponse = requests.get(nurl)
    nsoup = bs(nresponse.text, 'html.parser')
    news_title = nsoup.find("div", class_="content_title").get_text().strip()
    news_p = nsoup.find("div", class_='rollover_description_inner').get_text().strip()
    
    #JPL Mars SPace Images - Featured Image
    executable_path = {'executable_path': r'C:\Users\djhon\OneDrive\Desktop\GW_Repo\GWARL201902DATA3\01-Lesson-Plans\12-Web-Scraping-and-Document-Databases\2\Activities\07-Ins_Splinter\Solved\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    jplurl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jplurl)
    html = browser.html 
    soupjpl = bs(html, 'html.parser')
    clas = soupjpl.find_all('div', class_='carousel_items')
    
    for url in clas:
        urlfull = url.find('article')['style']
  
        
    url = urlfull.split("'",-1)[1]

    featured_image_url = 'https://www.jpl.nasa.gov' + url
    browser.quit()
    
    #Mars Weather
    turl = 'https://twitter.com/marswxreport?lang=en'
    tresponse = requests.get(turl)
    tsoup = bs(tresponse.text, 'html.parser')
    tweather = tsoup.find("div", class_="js-tweet-text-container").get_text()
    
    #Mars Facts
    furl = 'https://space-facts.com/mars/'
    ftables = pd.read_html(furl)
    df = ftables[0]
    df.columns = ['Title', 'Measures']
    mars_data = df.to_html()

    #Mars Hemispheres
    hurl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hresponse = requests.get(hurl)
    hsoup = bs(hresponse.text, 'html.parser')
    hsoup

    curl = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    cresponse = requests.get(curl)
    csoup = bs(cresponse.text, 'html.parser')
    clink = csoup.find_all('img', class_='wide-image')
    for link in clink:
            curlf = link['src']
    #print(curlf)


    surl = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    sresponse = requests.get(surl)
    ssoup = bs(sresponse.text, 'html.parser')
    slink = ssoup.find_all('img', class_='wide-image')
    for link in slink:
            surlf = link['src']
    #print(surlf)

    ssurl = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    ssresponse = requests.get(ssurl)
    sssoup = bs(ssresponse.text, 'html.parser')
    sslink = sssoup.find_all('img', class_='wide-image')
    for link in sslink:
            ssurlf = link['src']
    #print(ssurlf)

    vurl = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    vresponse = requests.get(vurl)
    vsoup = bs(vresponse.text, 'html.parser')
    vlink = vsoup.find_all('img', class_='wide-image')
    for link in vlink:
            vurlf = link['src']
    #print(vurlf)


    hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": 'https://astrogeology.usgs.gov' + curlf},
    {"title": "Valles Marineris Hemisphere", "img_url":'https://astrogeology.usgs.gov' + vurlf},
    {"title": "Schiaparelli Hemisphere", "img_url": 'https://astrogeology.usgs.gov' + surlf},
    {"title": "Syrtis Major Hemisphere", "img_url":'https://astrogeology.usgs.gov' + ssurlf},
    ]



   # Mars Data Dictionary
    mars_data = {
        'news_title' : news_title,
        'news_p' : news_p,
        'featured_image_url' : featured_image_url,
        'mars_weather' : tweather,
        'mars_facts' : mars_data, 
        'mars_hemispheres' : hemisphere_image_urls}

    # Close the browser after scraping
#    

    # Return results
    return mars_data
    #print(mars_data)
#scrape_info()
    