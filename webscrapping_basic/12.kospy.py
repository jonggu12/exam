import csv
import requests
import re
from bs4 import BeautifulSoup

url =  "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=" 





filename = "시가총액 1-200.csv" # csv의 파일 네임
f = open(filename, 'w',encoding = 'utf-8-sig', newline="") #csv 파일 오픈
writer = csv.writer(f)


title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)




for page in range(1,5):
    res = requests.get(url+ str(page)) # 1에서 4페이지
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    
    
    data_rows =  soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")  #전체의 row을 찾음
    for row in data_rows: #전체의 row 에서 하나씩 출력
        columns = row.find_all("td") # tr안에 td에 있는 모든 것들을 찾음
        if len(columns) <= 1: #의미없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns] # colums 에서 column의 반복문 실행하고 column.get_text를 추출
        # print(data)
        writer.writerow(data) # csv에 한 줄을 작성하는 함수
        