# 연산자

# 제곱 연산이되네?
print(2**4) # 예상 결과 : 16 

# 나머지 연산자는 알고있으니..
print(10 % 4) 

# 몫을 구하는 연산자 //
print(10 // 3)

# 비교 연산자
# 연산자는 다른 언어랑 비슷한가보네
# >, <, >=, <=, +=, *= 등
operatorNum: int = 3
operatorNum *= 5
print(operatorNum)
print(operatorNum == 15)
print(operatorNum != 15)
print(not (operatorNum == 15)) # True -> False
print(operatorNum and (3 < 5)) # Ture and True  => True (and == &)
print(operatorNum and (3 > 5)) # Ture and False => False

# or, | 생략.. 값 출력은 생략

# 숫자처리 함수
# 1. abs() = 절대값
print(abs(-5))

# 2. pow(값, 승수) = 제곱된 값
print(pow(5, 3)) # 125

# 3. max(값, 값) = 최대 값, min(값, 값) = 최소 값
print(max(5, 10), min(5, 10))

# 4. 반올림
print(round(3.17, 1)) # 결과 값 : 3.2 ... 소수점 두 번째 자리에서 반올림

from math import * # math 라이브러리 사용 선언
print("floor : ", floor(4.99)) # 내림
print("ceil : ", ceil(3.14))   # 올림
print("sqrt : ", sqrt(16))     # 제곱근 출력

# 랜덤함수
from random import *
print("random :", random()) # 0.0 ~ 1.0 미만의 임의의 값인데...숫자가 너무 애매한데?
print("random(1) :", int(random() * 10) + 1) # 1 ~ 11 미만의 랜덤 값 생성 
print("random(2) :", int(random() * 10) + 1)  
print("random(3) :", int(random() * 10) + 1)  

# 랜덤함수2
print("randRange : ", randrange(1, 46)) # 1 ~ 45 미만의 랜덤 값 생성

# 랜덤함수3
print("randint :", randint(1, 45)) # 1 ~ 45 '이하' 랜덤 값 생성 <- 이게 젤 편하네..