# 세트 (set)
# 중복이 안되고, 순서가 없다 (순서 보장 없음)
my_set:set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세찬"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집함
print(java | python)
print(java.union(python))

# 차집함 (java는 가능하지만 python은 모르는 사람)
print(java - python)
print(java.difference(python))

# 추가
python.add("김태호")
print(python)

# 삭제
java.remove("김태호")
print(java)

# 자료구조끼리 타입 변경이 가능하네? dictionary는 key-value의 형태라..이상한 형태로 출력
menu = {"커피", "우유"}
print(menu, type(menu))
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = dict(menu)
