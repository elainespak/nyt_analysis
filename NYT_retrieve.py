# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:10:37 2020

@author: elain
"""

### extract features

import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import DataFrame as df


class getFeatures(object):
    def __init__(self, url):
        self.url = url
        r = requests.get(url)
        html = r.text
        self.soup = BeautifulSoup(html,'html.parser')
        
    def get_upload_time(self):
        try:
            upload_time = self.soup.find('time')['datetime']
            self.upload_time = str(upload_time)           
        except:
            self.upload_time = None
        return self.upload_time
    
    def get_reporter_name(self):
        reporters = self.soup.find_all('span', class_="css-1baulvz")
        self.reporters_list = []
        for reporter in reporters:
            self.reporters_list.append(reporter.text)
        return self.reporters_list
    
    def get_section_type(self):
        try:
            self.section_type = self.soup.find_all('a', class_="css-nuvmzp")[0].text
        except:
            self.section_type = None
        return self.section_type
    
    def get_body(self):
        paragraphs = self.soup.find_all('p', class_='css-exrw3m evys1bk0')
        body = ''
        for p in paragraphs:
            body = body + ' ' + p.get_text()
        self.body = body.strip()
        return self.body
    
    def get_headline(self):
        try:
            title = self.soup.select('h1[itemprop=headline] > span')
            self.headline = title[0].text
        except:
            self.headline = None
        return self.headline
    
    def get_headline_length(self):
        if self.headline != None:
            return len(self.headline)
        else:
            return None
    
    def get_body_length(self): 
        if self.body != None:
            return len(self.body)
        else:
            return None
    
    def get_img_link(self):
        try:
            img = self.soup.find("img")
            img_src = img.get("src")
            self.img_url = img_src
        except:
            self.img_url = None
        return self.img_url

    def get_video_link(self):
        try:
            video_url = self.soup.select_one('p.vhs-data')
            self.video_url = video_url.find('a')['href']
        except:
            self.video_url = None
        return self.video_url

    def get_thumbnail(self):
        try:
            self.thumbnail = self.soup.find('picture').find('img')['src']
        except:
            self.thumbnail = None
        return self.thumbnail
