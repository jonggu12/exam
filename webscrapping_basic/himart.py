from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)


data_list = [] # 빈 데이터 리스트 만들기

for page in range(1, 6):
    url = f"https://www.e-himart.co.kr/app/display/showDisplayCategory?dispNo=1011020000&pageCount={page}"
    print("페이지:", page)
    driver.get(url)
    items = driver.find_elements(By.CSS_SELECTOR, ".prdItem.cateGoods")




    image_count = 1
    
    
    
    
    for item in items:
        
    
        try:
            # 제품 이름
            name = item.find_element(By.CLASS_NAME, "prdName").text
            
            
            price_info_element = item.find_element(By.CLASS_NAME, "prdPrice.priceTxt")

            # 기존 가격 (원래 가격)
            original_price_element = price_info_element.find_element(By.CLASS_NAME, "priceInfo").find_element(By.CLASS_NAME, "discountPrice")
            original_price = original_price_element.find_element(By.TAG_NAME, "strong").text.strip()
            
            # 할인된 가격 (discountPrice) #try문 두번쓰는 이유 첫번째 try문에서 예외가 발생하지 않으면 두번째 try문 을 실행하는데 가격과 이름이 예외가 발생하지 않아 두번째 try문도 실행
            # 기존 가격과 네임 평점 평점 수가 먼저 try가 되고 그 다음 할인된 가격이 try가 되기때문에 할인된 가격이 없을경우 할인된 가격 빼고 나머지 제대로 출력함
            try:
                
                discount_price_element = price_info_element.find_element(By.CLASS_NAME, "priceInfo.priceBenefit").find_element(By.CLASS_NAME, "discountPrice")
                discount_price = discount_price_element.find_element(By.TAG_NAME, "strong").text.strip()
                
            except:
                discount_price = "할인된 가격 없음"
            
            
            
            # 평점
            rate = item.find_element(By.CLASS_NAME,"ratingPoint").text
            # 평점 수
            rate_cnt = item.find_element(By.CLASS_NAME,"ratingTotal").text
            #링크
            link_element = item.find_element(By.CLASS_NAME, "prdLink")
            link_href = link_element.get_attribute("href")
             
        except:
            rate = "평점 정보 없음"
            rate_cnt = "평점 수 없음"
        
        

        
        
        
        #데이터 리스트에 추가
        data_list.append({
            '이름': name,
            '기존 가격': original_price,
            '할인된 가격': discount_price,
            '평점': rate,
            '평점 수': rate_cnt
        })
            
            
         #이미지 저장   
        image = item.find_element(By.CLASS_NAME,"prdImg").find_element(By.TAG_NAME,"img")

        image_url = image.get_attribute("src")

        if image_url.startswith("//"):
            image_url = "https://" + image_url

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        
        
        #이미지 저장하는 함수
        with open("./output/himart_{}페이지_{}등.jpg".format(page,image_count), "wb") as f:
           f.write(image_res.content)
        
        image_count += 1





        print("-"*50,'\n')
        print(f"제품명: {name}")
        print(f"원래 가격: {original_price}")
        print(f"할인된 가격: {discount_price}")
        print(f"평점: {rate}")
        print(f"평점 수: {rate_cnt}")
        print(f"바로가기: {link_href}")
        print("-"*50,'\n')
        
        # 데이터 프레임 생성
    final = pd.DataFrame(data_list)
    final.index = final.index+1
    final.to_csv('하이마트 냉장고 순위.csv', encoding='utf-8-sig')

    final      
    
driver.close()
        

        
                
            