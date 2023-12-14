




# 서기 연도를 알고 싶은 불기 연도 y가 주어짐 (1000<= y <= 3000)

# 불기 연도를 서기 연도로 변환하는 결과를 출력
# user_input = input("정수를 입력하세요: ")
# number = int(user_input)

# # 정수를 문자열로 변환한 후, 첫 번째 자릿수에 접근
# first_digit = str(number)[0]
# print("첫 번째 자릿수:", first_digit)



# A = int(input())
# B = int(input())


# e = str(B)[2]
# print(A*int(e))

# d = str(B)[1]
# print(A*int(d))

# c = str(B)[0]
# print(A*int(c))

# print(A*B)




# A,B,C = map(int,input().split())

# print(A+B+C)

# A*B
# A*B
# A*B
# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"`    |')
# print("||_/=\\\__|")


# A,B = map(int,input().split())


# if A>B:
#     print(">")
# elif A < B:
#     print("<")
# elif A == B:
#     print("==")
    
# else:
#     print("잘못입력했습니다.")

# A = int(input())

# if A >= 90 and A <= 100:
#     print("A")
# elif A >= 80 and A <= 89:
#     print("B")
# elif A >= 70 and A <= 79:
#     print("C")
# elif A >= 60 and A <= 69:
#     print("D")
# else:
#     print("F")




# |\_/|
# |q p|   /}
# ( 0 )"""\
# |"^"`    |
# ||_/=\\__|


# print("\\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \\(__)|")

# 3) 472 * 5     4) 472*8        5) 472*3     6) 472*385




# 윤년이면 == 1 , else: 0 을 출력


# 100, 200, 300 , 400, 500 ...
# 4, 8, 12 ,16 윤년 % 4 == 0 4로 나눴을때 나머지가 0이고  and 윤년이 100으로 나눴을때 나머지가 0이면 윤년이 아니다  or 윤년 % 400 == 0 이면 윤년
 
# 4의 배수이면서 100의 배수가 아니면 윤년
# 만약 1900년도는 100의 배수이고 400의 배수는 아니기때문에 윤년이 아님
# 2000년도는 400의 배수이기 때문에 윤년이다.


# year = int(input())

#     #연도는 1보다 크거나 같고, 4000보다 작거나 같은 자연수이다.
# if 1 <= year and year <=4000:
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         print("1")
#     else:
#         print("0")



# 1사분면 (+,+), 2사분면 (+,-), 3사분면 (-,-), 4사분면 (-,+)


# x = int(input())
# y = int(input())

# if x > 0 and y > 0: # 1사분면
#     print("1")
# elif x < 0 and y > 0: # 2사분면
#     print("2")
# elif x < 0 and y < 0: # 3사분면
#     print("3")
# elif x > 0 and y < 0: # 4사분면
#     print("4")
# else:
#     ("올바른 숫자를 입력하세요")



# 원래 알람시간에서 알람을 45분 일찍 설정
# H -> 시간 M -> 분

# ex) 10:10분  -> 9:25분
# 

# H, M = map(int,input().split())
# if M > 44:
#     print(H,M-45)
# elif H > 0 and M < 45:
#     print(H-1,M+15)
# else:
#     print(23,M+15)
    
    


# H, M = map(int, input("현재 시간과 분을 입력하세요 (예: 12 30): ").split())
# C = int(input("추가 분을 입력하세요: "))

# # 입력으로 받은 분에 추가 분을 더함
# M += C

# # 추가 분이 현재 증가하는 값 이상인 경우 시간과 분을 조정
# if M >= 60:
#     H += 1
#     M -= 60
# if M >= 120:
#     H += 2
#     M -= 120
# if M >= 180:
#     H += 3
#     M -= 180






# # 시간이 24시를 넘어가면 00으로 조정
# if H >= 24:
#     H = 0

# print("조정된 시간:", H, "시", M, "분")


H, M = map(int, input().split())
C = int(input())

M += C

if M >= 60:
    H += M // 60
    M %= 60

while H >= 24:
    H -= 24

print(H,M)
