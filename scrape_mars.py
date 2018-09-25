#-- code --#
import pandas as pd
from bs4 import BeautifulSoup as bs
import pymongo
from splinter import Browser
import time 


#-- code --#
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)

#-- code --#
# Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and 
# collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.
def news_title():
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
    one_soup = bs(browser.html, 'lxml')


    news_title = one_soup.find('div', class_="content_title").text
    
    return(news_title)

# news()
def news_article():
    url1 = 'https://mars.nasa.gov/news/'
    browser.visit(url1)
    one_soup = bs(browser.html, 'lxml')
    time.sleep(1)

    news_p = one_soup.find('div', class_="article_teaser_body").text

    return(news_p)
#-- code --#
# Visit the url for JPL Featured Space Image 
# [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).
# Use splinter to navigate the site and find the image url for the current
# Featured Mars Image and assign the url string to a variable called 
# `featured_image_url`.
# Make sure to find the image url to the full size `.jpg` image.
# Make sure to save a complete url string for this image.

# def featured_image(): 
#     url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
#     browser.visit(url2) 
#     browser.click_link_by_id('full_image')
#     time.sleep(1)
#     browser.click_link_by_partial_href('/spaceimages/details.php?id=')
#     time.sleep(1)
#     two_soup = bs(browser.html, 'lxml')

    
#     link = two_soup.find('div', id = "page-")
    
#     featured_image_url = url2 + link
#     return(featured_image_url)
# # featured_image()


def featured_image(): 
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2) 
    browser.click_link_by_id('full_image')
    time.sleep(1)
    two_soup = bs(browser.html, 'lxml')
    
    link = two_soup.find('img', class_ = "fancybox-image")
    featured_image_url = url2 + link['src']
    return(featured_image_url)
featured_image()
#-- code --#
# Visit the Mars Weather twitter account [here]
# (https://twitter.com/marswxreport?lang=en) and 
# scrape the latest Mars weather tweet from the page. 
# Save the tweet text for the weather report as a variable 
# called `mars_weather`.
def weather():
    url3 = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url3) 
    three_soup = bs(browser.html, 'lxml')    

    mars_weather = three_soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    return(mars_weather)
# weather()

#-- code --#
# Visit the Mars Facts webpage [here](http://space-facts.com/mars/) 
# and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
# Use Pandas to convert the data to a HTML table string.
def facts(): 
    url4 = 'http://space-facts.com/mars/'
    # browser.visit(url4) 
    # four_soup = bs(browser.html, 'lxml')

    tables = pd.read_html(url4)
    df1 = tables[0]
    df1.columns=["Category", "Measurement"]
    df1=df1.iloc[1:]
    df1 = df1.set_index("Category")
    return(df1.to_html('table.html'))
# facts()    

#-- code --#
#df1.to_html('table.html')
#!open table.html

#-- code --#
### Mars Hemispheres
#Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) 
# to obtain high resolution images for each of Mar's hemispheres.
#You will need to click each of the links to the hemispheres in order to 
# find the image url to the full resolution image.
#Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys `img_url` and `title`.
#Append the dictionary with the image url string and the hemisphere 
# title to a list. This list will contain one dictionary for each hemisphere.
def hem_url_img():

    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5) 

    links = [(x.text, x['href']) for x in browser.find_by_css(
        'div[class="description"] a[class="itemLink product-item"]'
    )]

    hemisphere_image_urls = []
    for link in links:
        browser.visit(link[1])
        img_url = browser.find_by_css('img[class="wide-image"]')['src']
        hemisphere_image_urls.append({
            'title': link[0].replace(' Hemisphere Enhanced', ''),
            'img_url': img_url,
        })
    return(hemisphere_image_urls)
# hem_url_img()

#-- code --#
# Start by converting your Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
def scrape():
    news_title2 = news_title()
    news_article2 = news_article()
    featured_image2 = featured_image()
    weather2 = weather()
    facts2 = facts()
    hem_url_img2 = hem_url_img()
    
    dict_ = {'news_title': news_title2, 'article': news_article2, 'image': featured_image2, 'weather': weather2, 'facts_table': facts2, "hem": hem_url_img2}
    return(dict_)


#scrape()
    
     

#-- code --#


