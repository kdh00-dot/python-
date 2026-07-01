# 문자열 길이 구하기 (len 함수)
a = "life is too short"
print(len(a))
# 17

# 인덱싱(indexing) []
# 내가 원하는 글자를 집어서 가져오는 것
a = "life is too short"
#a[] 는 a에있는 몇번째를 가리킨다
print(a[0])  # 0번 방에 있는 'l' 출력
print(a[3])  # 3번 방에 있는 'e' 출력
print(a[4])  # 4번 방에 있는 ' ' (빈칸/공백) 출력
# 공백도 번호를 가지고 있다
# 0부터 시작하고 뒤에서는 -1부터 시작

# 슬라이싱(slicing) [시작 : 끝] 형태 끝 번호에 해당 문자 포함 안함
# 둘 다 생략 [:] 처음부터 끝까지 전체 다 복사
a = "Life is too short, You need Python"
print(a[0:2])
# 'Li'
print(a[5:7])
# 'is'
print(a[12:17])
# 'short'

# 슬라이싱으로 문자열 나누기
a = "20260701Rainy"
date = a[:8]
weather = a[8:]
print(date)
# '20260701'
print(weather)
# 'Rainy