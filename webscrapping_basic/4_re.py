import re #정규식

# abcd, book, desk
# ca?e
#care, cafe,case,cave
# caae, cabe, cace,...

p = re.compile("ca.e") 

# . (ca.e) > 하나의 문자를 의미 > care,cafe, case 
#^ (^de): 문자열의 시작을 의미 > desk, destination (O) |fade (x)
# $ (se$) : 문자열의 끝 > case, base (O) | face(X)
def print_match(m):
    if m:
        print("group:",m.group()) #일치하는 문자열 반환
        print("string",m.string) #입력받은 문자열
        print("start:",m.start()) #일치하는 문자열의 시작 Index
        print("end:", m.end()) #일치하는 문자열의 끝 index
        print("span:",m.span()) # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭X")
        
# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lis = p.findall("good care cafe")
# print(lis)


# 1. re.compile("원하는 형태") 로 컴파일을 함

# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인

# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인

# 4. list = p.findall("비교할 문자열") : 일치하는 모든 것을 리스트 형태로 변환

# 원하는 형태 : 정규식
# . (ca.e) > 하나의 문자를 의미 > care,cafe, case 
#^ (^de): 문자열의 시작을 의미 > desk, destination (O) |fade (x)
# $ (se$) : 문자열의 끝 > case, base (O) | face(X)