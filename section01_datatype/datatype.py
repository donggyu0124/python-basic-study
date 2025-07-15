# 자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(4 + 6)
print(2 * 10)
print(3 * (3 + 1))

# 문자열
# 따옴표 처리지만 익숙한 문자열 방식으로 "" 형식으로 사용
# print('풍선') 
# print("나비")

# 이런 연산이 가능한가? 신기하네 
print("HA " * 5) 

# 참 / 거짓 (BOOLEAN)
# not이 그럼 ! 연산자네
print(5 > 10)
print(5 < 10)
print(5 <= 5)
print(True)
print(False)
print(not True)
print(not (5 > 10)) # !False => True

# 변수 사용법
# 변수는 :자료형으로 명시적으로 해주는게 좋을듯
# 문자열은 str(var) 사용법이 .toString() 함수 사용 같은 방식이네
name: str = "동규"
count: int = 2
isAdult: bool = (37 >= 20)
print(name + "는 성인이니? " + str(isAdult))
print(name + "는 커피 마시는걸 좋아해요.")
print(name + "는 하루에 커피를 " + str(count) + "잔 마셔요.")

# 문자열 + 변수 합치는 법 (2)
# , 는 문자열이 아닌 다른 변수 타입을 문자열로 변경하지 않아도된다.
job: str = "RPA 분야를 준비중이야 !"
print("안녕? 나는", job)