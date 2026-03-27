# 파이썬의 조건문 연습
"""
if 조건 :
    실행문
else :
    실행문
"""
# 파이썬의 코드 블럭은 들여쓰기로 구분
# 들여쓰기는 공백 4칸 혹은 탭
# 섞어 사용하면 안됩니다

x = 4
if x % 2 == 0 :
    print("짝수")
else :
    print("홀수")    

age = 53
if (age // 10) < 2 :
    print("10대")
elif ( age // 10 ) == 2:
    print("20대")
elif ( age // 10 ) == 3:
    print("30대")    
else:
    print("40대 이상")    

# 다음 x값이 3과 5의 공배수이면 "공배수"입니다.
# 그렇지 않으면 "공배수 아님" 이라고 출력하세요.
x = 15
if (x % 3 == 0) and (x % 5 == 0) :
    print("공배수")
else :
    print("공배수 아님")
    
# 키보드로 점수를 입력 받아서
# 90점 이상 : A 학점
# 80점 이상 : B 학점
# 70점 이상 : C 학점
# 70점 미만 : 낙제
# 라고 표시하세요.

score = int( input("점수:") )
if score >= 90 :
    print("A 학점")
elif score >= 80 :
    print("B 학점")
elif score >= 70 :
    print("C 학점")    
else :
    print("낙제")    

