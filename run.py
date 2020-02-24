# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 00:14:26 2020

@author: elain
"""

from NYT_retrieve import *


### bring pickle files
import pickle
    
# open a file, where you stored the pickled data
folder_path = 'Twitter_data/'
file = open(folder_path + 'all_nyt_twitter.p', 'rb')

# dump information to that file
data = pickle.load(file)

# close the file
file.close()


### collect
features_data = {k:v for k,v in list(data.items())[8000:20000]} # so far: 0~16153

i = 0
for url, v in features_data.items():
    features = getFeatures(url)
    
    new_features = (features.get_reporter_name(),
    features.get_section_type(),
    features.get_upload_time(),
    features.get_body(),
    features.get_headline(),
    features.get_body_length(),
    features.get_headline_length(),
    features.get_img_link(),
    features.get_video_link(),
    features.get_thumbnail()
    )
    
    features_data[url] += new_features
    i += 1

# save data to a pickle file
folder_path = 'Twitter_data/'
file_name = folder_path + 'test_nyt_features3.p'
with open(file_name, 'wb') as fp:
    pickle.dump({k:v for k,v in list(features_data.items())[:8153]}, fp, protocol=pickle.HIGHEST_PROTOCOL)

fp.close()

'''
features_data_list = list(features_data.items())

### count data where web scraper did not work
idx = 0
for i in features_data_list:
    if i[1][-7] == '':
        idx+=1
        #print(i[0])
        #print(f'section type: {i[1][-9]}')
        #print(f'upload time: {i[1][-8]}')
        #print(f'headline: {i[1][-6]}')
        #print('\n')
print(idx)
'''