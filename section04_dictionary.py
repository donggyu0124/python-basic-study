# 사전
# Key - Value

cabinet:dict = {1: "철수", 2:"영희"}

# 가져오기
# 직접 접근하여 값을 가져오는 경우 키가 없다면 '에러' 후 프로그램 종료
# get 함수를 통하여 가져오는 경우 키가 없다면 'None' 출력
print(cabinet[1])
print(cabinet.get(2))
print(cabinet.get(3)) # None 출력
print(cabinet.get(3, "Default Value")) # None대신 기본 값 출력

# 키 체크
# 'key' in Dictionary
print("2 int cabinet :", 2 in cabinet)
print("3 int cabinet :", 3 in cabinet)

# 키 값은 문자열도 가능
cabinetStr = {"A-3":"짱구", "A-4":"짱아"}
print(cabinetStr.get("A-4"))

# 추가 > 이미 키가 있다면? 값 업데이트
cabinetStr["A-5"] = "맹구"
print("\"A-5\"키에 해당하는 값:", cabinetStr["A-5"])
cabinetStr["A-5"] = "훈이"
print("\"A-5\"키에 해당하는 값:", cabinetStr["A-5"])

# 삭제
del cabinetStr["A-5"]
print(cabinetStr)

# key만 출력
print(cabinetStr.keys())

# value만 출력
print(cabinetStr.values())

# key - value 출력
print(cabinetStr.items())

# 전부 삭제
cabinetStr.clear()
print("clear :", cabinetStr)