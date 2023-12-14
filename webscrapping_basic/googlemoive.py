from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import pandas as pd


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=chrome_options)



url = f"https://play.google.com/store/movies?hl=ko&gl=US"
driver.get(url)
items = driver.find_elements(By.CSS_SELECTOR, ".VfPpkd-WsjYwc.VfPpkd-WsjYwc-OWXEXe-INsAgc.KC1dQ.Usd1Ac.AaN0Dd.MPNOXb")


image_count = 1

data_list = []

for item in items:
    
   
    name = item.find_element(By.CLASS_NAME, "ubGTjb").text
    price = item.find_element(By.CSS_SELECTOR, ".w2kbF.ePXqnb").text
    link_element = item.find_element(By.CSS_SELECTOR, ".Si6A0c.itIJzb")
    link_href = link_element.get_attribute("href")

    
    # 장르의 모든 요소 가져오기
    genre_elements = item.find_elements(By.CLASS_NAME, "cXFu1")
    # 장르 추출
    for genre_element in genre_elements:
        genre = genre_element.find_elements(By.CLASS_NAME, "ubGTjb")
                                            
        # 추출할 인덱스 지정
        if len(genre) == 4:
            target_index = 2  # 4개인 경우 3번째 요소를 추출 
        elif len(genre) == 3:
            target_index = 1  # 3개인 경우 2번째 요소를 추출  
        else:
            print("예상하지 못한 상황입니다.")

        # 인덱스가 범위 내에 있는지 확인하고 추출
        if 0 <= target_index < len(genre):
            genre = genre[target_index].text
        
        else:
            print(f"{target_index + 1}번째 요소는 존재하지 않습니다.")
        
    
    
    #평점 추출
    
        
    for rate_element in genre_elements:
        rate = rate_element.find_elements(By.CLASS_NAME, "ubGTjb")
                                            
        # 추출할 인덱스 지정
        if len(rate) == 4: # rate의 ubGTjb 클래스가 4번째에 있을 경우 3번째 추출하면 평점이 나옴
            target_index = 3
            rate_text = rate[target_index].find_element(By.CLASS_NAME,"w2kbF").text                                      #  4개인 경우 4번째 요소 추출
        elif len(rate) == 3:
            target_index = 2  # rate의 ubGTjb 클래스가 3개인 경우 3번째 요소를 추출하면 평점이 나옴
            rate_text = rate[target_index].find_element(By.CLASS_NAME,"w2kbF").text  
        else:
            print("예상하지 못한 상황입니다.")


        image = item.find_element(By.CLASS_NAME,"j2FCNc").find_element(By.TAG_NAME,"img")

        image_url = image.get_attribute("src")

        if image_url.startswith("//"):
            image_url = "https://" + image_url

        image_res = requests.get(image_url)
        image_res.raise_for_status()

        
        
        #데이터 리스트에 추가
        data_list.append({
            '이름': name,
            '기존 가격': price,
            '할인된 가격': genre,
            '평점': rate_text,
            '링크': link_href
        })
        
        
        
        #이미지 저장하는 함수
        with open("./output/googlemovies_{}등.jpg".format(image_count), "wb") as f:
           f.write(image_res.content)
        
        image_count += 1
        
        
        
        
    print("-"*50)
    print(f"영화 제목 : {name}")
    print(f"가격 : {price}")
    print(f"장르 : {genre}")
    print(f"평점 : {rate_text}")
    print(f"링크 :{link_href}")
    print("-"*50,'\n')
    
    final = pd.DataFrame(data_list)
    final.index = final.index+1
    final.to_csv('구글 영화 순위.csv', encoding='utf-8-sig')

    final



    

driver.close()