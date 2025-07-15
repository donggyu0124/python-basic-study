# 튜플
# 속도는 리스트보다 빠르나, 변경할 수 없다. (정적 데이터)

menu:tuple = ("돈까스", "제육")
print(menu[0])
print(menu[1])

name = "철수"
age = 20
hobby = "독서"
print(name, age, hobby)

# 튜플 형태긴한데...클래스 이후 뭔가 사용될듯한데
(name, age, hobby) = ("맹구", 20, "수집")
print(name, age, hobby)