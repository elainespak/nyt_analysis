# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 16:10:37 2020

@author: Elaine Pak
"""

### call libraries

import GetOldTweets3 as got
import re
import pickle


### collect data (오래 걸릴 수 있음, 구간별로 쪼개서 해도 됨)
start_date = "2018-08-01" #시작날짜 (시작날짜 데이터도 수집됨) *--- 수정 ---*
end_date = "2019-01-01" #끝날짜 (끝날짜 데이터는 수집되지 않음) *--- 수정 ---*

tweetCriteria = got.manager.TweetCriteria().setUsername("nytimes")\
                                           .setSince(start_date)\
                                           .setUntil(end_date)\
                                           .setMaxTweets(0)\
                                           .setEmoji("unicode")    

alltweets = got.manager.TweetManager.getTweets(tweetCriteria)
print(len(alltweets)) #대충 하루에 100개 정도 수집됨

tweets_dict = {} #데이터가 많으니 dictionary를 사용해 pickle 파일로 저장
                                 
# get the relevant features from the collected data     
for i in range(len(alltweets)):
                                 
     tweet = alltweets[i].text
     try:
          url = 'http://' + re.findall('(?<=http://).*(?=\s)', tweet)[0] #기사 링크
          text = re.findall('.*(?=http://)', tweet)[0] #트윗의 text 내용 (1~2줄)
     except:
          url = ''
          text = tweet
          
     if 'pic.twitter.com/' in tweet:
          pics = re.findall('pic.twitter.com/[a-zA-Z0-9]*', tweet) #사진 링크 (없는 경우도 있음)
     else:
          pics = [] #없으면 empty list로 저장
     
     date = alltweets[i].date #트윗이 올라온 시간
     like = alltweets[i].favorites #좋아요 갯수
     retweet = alltweets[i].retweets #리트윗 갯수
     reply = alltweets[i].replies #트윗의 댓글 갯수
     
     tweets_dict[url] = (text, pics, date, like, retweet, reply)
     
     # sanity check
     if i%100 == 0:
          print(f'{i} tweets scraped') #코드가 잘 돌아가는지 중간중간 확인 용도
print(f'Done extracting features from all {len(alltweets)} tweets!')

# save data to a pickle file
folder_path = 'Twitter_data/'
file_name = folder_path + start_date + '_to_' + end_date + '_nyt_twitter.p'
with open(file_name, 'wb') as fp:
    pickle.dump(tweets_dict, fp, protocol=pickle.HIGHEST_PROTOCOL)

fp.close()
