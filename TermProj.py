# 케글(https://www.kaggle.com/datasets)에서 수집한 자료입니다.
# 케글 홈페이지의 표에서 웹 크롤링이 불가능하여 csv파일을 받아 사용하였습니다.
#from bs4 import BeautifulSoup
#from urllib.request import *

#html = urlopen("https://www.kaggle.com/omkarborikar/top-10000-popular-movies?select=Top_10000_Movies.csv")
#soup = BeautifulSoup(html, "html.parser")

#print(soup)
#print(soup.title)

#aa = soup.find('div', id="site-container").find('div')
#aa = soup.select_one('#site-content > div.Dataset_Wrapper--isllmh.iCQOLe > div.Home_Wrapper--1lm6bf2.iakMUi > div:nth-child(3) > div.sc-ljsFck.eDtiWG > div > div.sc-fhOcgi.gwTFcQ > div > div.sc-ilUONv.dAhsL')
#print(aa)

import pandas as pd
import matplotlib.pyplot as plt

csvdata=pd.read_csv("Top_10000_Movies.csv", nrows=10000).iloc[:,[2,3,4,5,6,8]]
csvdata.columns = ['lang','title','popularity','release','vote_mean', 'genre']

# 1. 언어 별 영화 수 세기
# print(csvdata['lang'].value_counts())

# 2. 언어 별 평균 평점 및 평균 인기도 
# print(csvdata.groupby('lang')['vote_mean','popularity'].mean())
# print(csvdata)

# 조건에 맞는 영화 검색(5점 이상, 최소 2010-01-01년작인 한국어 영화)
'''filt = (csvdata['vote_mean'] > 5) & (csvdata['release'] > ('2010-01-01')) & (csvdata['lang'] == 'ko')
kordata = csvdata[filt]
print(kordata[['title', 'vote_mean']])'''

# 선택한 장르의 영화 검색
'''i = 0
while(i<csvdata.shape[0]):
    if 'Thriller' in csvdata['genre'][i]:
        print(csvdata['title'][i])
    i +=1'''


'''genre=[]
chars="'[],"
for genres in csvdata['genre']:
    if i in ''.join(x for x in genres if x not in chars).split():
    #if i in item not in genre:
    #    genre.append(item)
print(genre)'''


'''import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array(csvdata['vote_mean']).reshape(-1,1)
y = csvdata['popularity']
lr = LinearRegression()
lr.fit(X, y)
#print(lr.coef_)

w = lr.coef_[0]

plt.scatter(X, y, s=1)
plt.plot(X, w*X, c='red')''''''