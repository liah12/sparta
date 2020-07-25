import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
baseballRank = soup.select('#regularTeamRecordList_table > tr')

for baseball in baseballRank:

    th_tag = baseball.select_one('th > strong')
    td_tag = baseball.select_one('td.tm > div > span')
    td_strong_tag = baseball.select_one('td:nth-child(7) > strong') #nth-child(몇번쨰) 클래스가 없을 경우 정확한 것을 부분을 출력할 수 있다.

    #if th_tag is not None and td_tag is not None:
       #value = th_tag.text + " " + td_tag.text + " " + td_strong_tag.text    #value 변수 지정
    if float(td_strong_tag.text) > 0.5:
        value = th_tag.text + " " + td_tag.text + " " + td_strong_tag.text  # value 변수 지정
        print (value)
        #print(th_tag, td_tag, td_strong_tag)