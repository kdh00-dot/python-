# 문자열 ( 따옴표로 둘러싸여 있으면 모두 문자열이다 )
#string
"Hello world"
'python in fun'
"""Life in too short, You need python"""
'''Life in too short, You need python'''

# 문자열에 작은따옴표 포함하기
food = "Python's favorite food is perl"
food
# "Python's favorite food is perl"

# 큰따옴표 포함하기
say = '"Python is very easy" he say'
say
# '"Python is very easy" he say'

# 역슬래시를 사용해 작은따옴표와 큰따옴표를 포함하기
food = 'python\'s favorite food is pear'
say = "\"Python is very easy.\" he says."
# \를 작은따옴표나 큰따옴표 앞에 삽입하면 역슬래시뒤의 작은따옴표나 큰따옴표는
# 문자열을 둘러싸는 기호가 아니라 문자 그 자체를 뜻함.

# 연속된 작은따옴표3개, 큰따옴표3개 사용
multiline = '''
Life is too short
You need python
'''
print(multiline)
#Life is too short
#You need python

# 문자열 더해서 연걸하기
head = "Python"
tail = "is fun!"
head + tail 
# 'Pythom is fun!'

# 곱하기 
a = 'Python'
a * 2
#'PythonPython'