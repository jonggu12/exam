import requests


url = "http://nadocoding.tistory.com"

headers = {"User-Agent":"Mozilla/5.0(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status() #문제가 생기면 발생

with open("nadocoding.html","w",encoding="utf8") as f:
    f.write(res.text)