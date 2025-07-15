# 문자열

sentence:str = "안녕"
print(sentence)

sentence = "파이썬 공부중이야~"
print(sentence)

# 이렇게 여러줄을 만들 수 있네
sentence = """
안녕
파이썬 공부중이야~
"""
print(sentence)

# 문자열 자르기
number = "012345-678910"
print("문자열 자르기(1) :", number[7])
print("문자열 자르기(2) :", number[0:2]) # 0 부터 2 직전까지 이런 형식은 처음보네
print("문자열 자르기(3) :", number[:5])  # : 으로 시작하면 처음부터 시작
print("문자열 자르기(4) :", number[7:])  # : 으로 끝내면 끝 자리까지
print("문자열 자르기(5) Reverse :", number[-6:])  # 맨 뒤에서 6번째부터 끝까지 .. 그런데 쓸일이 있을까 ?

# 문자열 처리 함수
# 1. 문자열 대/소문자 처리
print("HEllO WORLD".lower())
print("hello world".upper())

# 2. 대/소문자 확인
print("Python".isupper())    # False
print("Python"[0].isupper()) # True
print("python".islower())    # True

# 3. 문자열 길이
print(len("My name is DonggyuKim"))

# 4. 특정 문자열 바꾸기
_str:str = "Python is Simple"
print(_str.replace("Python", "C#"))

# 5. 문자열 찾기(1) = index (= 대소문자를 구별하네?)
print(_str.index("s"))
_str = "simple / simple";
print(_str.index("s", 5)) # 두번째 매개변수는 시작위치

# 6. 문자열 찾기(2) = find
print(_str.find("Java"))    # find 함수는 찾는 문자열이 없으면 -1 리턴
# print(_str.index("Java"))   # index 함수는 에러 출력

# 7. 특정 문자열이 몇번 등장하는지 체크
_str = "python python python !!!"
print(_str.count("python"))
