#파이썬의 데이터 형식 (자료형)
#리스트, 튜플, SET, 딕셔너리

#리스트 타입 연습
data = [1, 2, 3, 4]
print("변수타입:", type(data))
print("원소개수:", len(data))
print("=" * 40)

data = [ 1, "감", 3.14, "고구마" ]
print(data[1])
print("=" * 40)

#튜플(tuple) 타입 연습
#튜플은 등록/수정/삭제 불가
data = (1, 2, 3, 4)
print("변수타입:", type(data))
print("원소개수:", len(data))
print("=" * 40)

#set 타입 연습
#set 은 중복된 원소 값은 허용하지 않음.
data = {1, 2, 3, 4, 1, 2, 3, 4, 1}
print(data)
print("변수타입:", type(data))
print("원소개수:", len(data))
print("=" * 40)

#딕셔너리(사전) 타입 연습
#Key와 Value를 쌍으로 저장하는 자료형
data = { "홍길동" : "도적" , "성춘향" : "기생" }
print("변수타입:", type(data))
print("원소개수:", len(data))
print("=" * 40)

#딕셔너리는 값을 조회 할 때 키로 조회한다.
print(data["성춘향"])
print("=" * 40)




