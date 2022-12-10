from urllib import response
import pandas as pd
import requests
from bs4 import BeautifulSoup 
import re
from html_to_etree import parse_html_bytes
from extract_social_media import find_links_tree



def get_phone(soup):
    try:
        phone = soup.select("a[href*=callto]")[0].text
        return phone
    except:
        pass

    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', response.text)[0]
        return phone
    except:
        pass

    try:
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', response.text)[-1]
        return phone
    except:
        print ('Phone number not found')
        phone = ''
        return phone



def get_email(soup):
    try:
        email = re.findall(r'([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)', response.text)[-1]
        return email
    except:
        pass

    try:
        email = soup.select("a[href*=mailto]")[-1].text
    except:
        print ('Email not found')
        email = ''
        return  email

def get_social(soup):
    url = BeautifulSoup(soup.text, 'html.parser')
    for link in url.find_all('a'):
        href = link.get('href')
        if 'https://www.facebook.com/' in href:
            print(href)
        if 'https://www.linkedin.com/' in href:
            print(href)
        if 'https://www.twitter.com/' in href:
            print(href)
        if 'https://twitter.com/'in href:
            print(href)

url = 'https://ful.io/'
response = requests.get(url)
get_social(response)
print("Email/s- \n",get_email(response))
print("Contact: \n",get_phone(response))