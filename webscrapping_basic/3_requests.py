import requests


res1 = requests.get("http://google.com")

res1.raise_for_status() #문제가 생기면 발생
print("웹스크래핑을 진행합니다")



# print("응답코드:",res1.status_code) # 200이면 정상

# if res1.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print(res1.status_code)

# print(len(res1.text))
# print(res1.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res1.text)