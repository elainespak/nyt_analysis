from bs4 import BeautifulSoup
import requests
import pandas as pd
from pandas import DataFrame as df

def get_basic_soup(url):
    r=requests.get(url)
    html=r.text
    soup=BeautifulSoup(html,'html.parser')
    return soup

def headline_len(soup):
    try:
        title=soup.select('h1[itemprop=headline] > span')
        headline_len=len(title[0].text)
        return headline_len
    except:
        return ''

def body_len(soup):
    try:
        body=soup.select('p')
        body_len=len(body[4].text)
        for i in range(5,len(body)-2):
            body_len += len(body[i].text)
        return body_len
    except:
        return ''

def img_url(soup):
    try:
        img=soup.find("img")
        img_src=img.get("src")
        return img_src
    except:
        return ''

def dataframe(url):
    try:
        df_soup=df(data={'url':[url],'headline_len':[headline_len(soup)],'body_len':[body_len(soup)],'img_url':[img_url(soup)]})
        return df_soup
    except:
        return ''

url = 'https://www.nytimes.com/2020/01/21/us/politics/barr-impeachment-abuse-of-power.html?action=click&module=Top%20Stories&pgtype=Homepage'
soup=get_basic_soup(url)
print(headline_len(soup))
print(body_len(soup))
print(img_url(soup))
print(dataframe(url))
