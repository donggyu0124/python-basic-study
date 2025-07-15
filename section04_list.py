# 리스트
# 순서를 가지는 객체의 집합 .. 배열이긴한데 타입에 상관없는 배열이네

subway = [10, 20 , 30, "hello"]
print(subway)
print("subway[0] : {count}, subway[1] : {name}".format(count = subway[0], name = subway[3]))
print(f"subway[0] : {subway[0]}, subway[1] : {subway[3]}")

nameList:list = ["철수", "영희", "짱구"]
print(nameList.index("영희"))

# 리스트 추가
# append = 맨 뒤에 추가
nameList.append("짱아")
print(nameList)

# insert = 특정 위치에 추가
nameList.insert(2, "맹구")
print(nameList)

# pop = 맨 뒤에 꺼내기 (리스트에서 꺼내면 리스트에선 사라진다.)
print(nameList.pop())
print(nameList)

# 같은 값이 얼마나 있는지 확인
nameList.append("철수")
print(nameList)
print(nameList.count("철수"))

# 정렬
numList:list = [0, 3, 5, 2, 9, 7]
numList.sort(); # 오름차순
print(numList)
numList.reverse() # 내림차순
print(numList)

# 모두 지우기
# numList.clear()
print("clear numList : " + str(numList))

# 리스트 합치기
nameList.extend(numList) # nameList에 numList를 합치는 함수
print(nameList)