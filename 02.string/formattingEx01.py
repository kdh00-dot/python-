#문자열 포매팅 (Formatting) 문자열 안에 변하는 숫자나 글자를 편리하게 채워 넣기 위해 사용
#f-문자열 (f-string)문자열 앞에 f를 붙이고 중괄호 {} 안에 변수를 바로 넣는 방식입니다.
name = "철수"
age = 20

print(f"이름은 {name}이고, 나이는 {age}살입니다.")
# 사직연산의 결과 출력 
num1 = int(input("첫 번째 정수를 입력하세요"))
num2 = int(input("두 번째 정수를 입력하세요"))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")