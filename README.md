# Online Contents Popularity Analysis with New York Times (NYT) data

## Objective

**Why analyze online contents popularity?** In the digital era, everyone is competing for attention. Our goal is to analyze the relationship between online contents and their popularity.

**NYT data is ideal for performing the above task.** Every single NYT article gets tweeted on NYT's Twitter account as a separate tweet, making it possible to measure the popularity level of each article by considering number of Likes, number of Retweets, and number of Comments on each tweet.

The idea was inspired by the following paper: [What makes online content viral?](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1528077)

## Methodology

1. [GetOldTweets3](https://pypi.org/project/GetOldTweets3/) package was used to scrape basic information regarding each article and the corresponding popularity level from the @nytimes Twitter acount.
1. Hand-written web scraper was built to extract features from each article. In building the web scraper, we mostly used regular expression and BeautifulSoup4.
1. Then we performed feature engineering to obtain features such as the sentiment polarity (positive vs. negative) of each article.
1. Lastly, we observed the relationship between the gathered features and the popularity measure, measured by number of Likes, number of Retweets, and number of Comments of each Tweet.

## Scope of Data

Approximately 100 articles are released each day. We initially analyzed data from 2016-04-01 through 2016-07-01. 

## List of Features
To be organized..


## Team
* PM: Elaine Pak (member of [Data Mining Center](http://dm.snu.ac.kr/en/), Seoul National University)
* Interns: Sunbin Kwon, Hyeonjin Kim, Jaehyeon Nam, Yongjae Lee, Jaesung Lee, Hanyong Lee
