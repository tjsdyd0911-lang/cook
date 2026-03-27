# 문자열 다루기 연습
s = "abcdefghijklmnop"

# 문자열 길이
print(len(s))
print("=" * 40)

# 문자열 인덱싱
# 인덱싱은 [] 를 사용하고 [] 안에 인덱싱 할
# 원소 번호를 이용한다. 인덱싱 번호는 0부터 시작
print(s[0])  #0번째 원소 a를 출력한다.
print("=" * 40)

print(s[1])  #1번째 원소 b를 출력한다.
print("=" * 40)

# 인덱스의 범위 지정 => : 을 사용한다.
#s = "abcdefghijklmnop"
print(s[5])    #5번 원소만 
print(s[0:5])  #0~4번 원소까지 출력
print(s[2:5])  #2~4번 원소까지 출력
print(s[:5])   #0~4번 원소까지 출력
print(s[2:])   #2번 원소에서 끝까지 출력
print(s[-5])   #끝에서 -5번째 원소
print(s[-5:-2])#끝에서 -5번째 원소 ~ -2번째까지

#인덱스 연습문제
s = "0123456789"
t = s[:5]
print(t)       #t = "01234"
print(t[2:4])  #아래 코드와 동일
print(s[:5][2:4]) 


# 인덱싱을 이용하여 날짜만 출력하세요
# 인덱싱을 이용하여 시간만 출력하세요
now = "2024-05-07 16:37:32"
print("날짜:",now[:10])
print("시간:",now[11:])

print("날짜:",now[0:10])
print("시간:",now[-8:])

# 앞뒤 공백 제거
s = "  ab c   "
print(len(s))
s = s.strip()
print(len(s))
print(s)

# 문자열 자르기
now = "2024-05-07 16:37:32"
ary = now.split(" ")
print(ary[0])
print(ary[1])

# 문자열 치환
s = "abc abc aaa"
t = s.replace("a","A")
print(t)

# boolean  타입
flag = True
print(type(flag))

flag = False
print(type(flag))

#비교 연산자
# >, >=, <, <= , ==, !=
flag = 10 > 20
print(flag)

flag = 10 >= 10
print(flag)

flag = 10 < 20
print(flag)

flag = 10 <= 20
print(flag)

flag = 10 == 20
print(flag)

flag = 10 != 20
print(flag)

# 논리 연산자
# &&, ||, !
# and, or, not
age = 16
flag = ( age < 18 ) and ( age > 60 )
print(flag)

flag = ( age < 18 ) or ( age > 60 )
print(flag)







