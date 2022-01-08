#!/usr/bin/env python
# coding: utf-8

# ## Mission to Mars Web Scrape

# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}

browser = Browser('chrome', **executable_path, headless=False)

## assign the url and instruct the browser to visit it
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

## set up html parser
html = browser.html
news_soup = soup(html, 'html.parser') ## soup means beautiful soup
slide_elem = news_soup.select_one('div.list_text')

## use inspect to find the title and paragraph on the webpage
## find the html tag and call it with .find
## find it inside slide_elem
slide_elem.find('div', class_='content_title')

## we need to take out the extra html
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

## find the teaser paragraph and change the class
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p

# ### Featured Images

## we want to get mars images from the jpl website
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# make new variable, browser finds an element by its tag, splinter will 
## click the button for you
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

## the previous code searched for the image url and this code will create the actual url
# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

## we want to get mars images from the jpl website
# Visit URL
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)

## use pandas to read the html table
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df

## you can change this table format back into html
df.to_html()

## always turn off the automated session
browser.quit()




