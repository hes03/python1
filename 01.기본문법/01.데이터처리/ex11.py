#문자열 함수
str = 'python is amazing'
print(str.lower())  #소문자로
print(str.upper())  #대문자로
print(str.capitalize()) #첫번째 문자 대문자로
print(str[0].islower()) #첫번째가 소문자인지
print(len(str))
print(str.replace('python', '파이썬'))

index = str.index('a')  #a가 몇번째인지
print(index)
print(str[index:].upper())
# print(str.index('ab')) --> 없는경우 error

print(str.find('a'))
print(str.find('ab'))  # 없는 경우에도 오류X. -1

print(str.count('i'))
print(str.count('is'))