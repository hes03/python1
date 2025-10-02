#나이, 성별 입력 받아 여탕에 들어갈 수 있을까 알아보는 조건
#조건: 여자이거나 남자이면서 4세미만
print('여탕에 입장가능?')
age = int(input('나이>'))
gender = input('성별>')
result1 = (gender == '여') or (gender == '남' and age < 4)
print(f'결과는 {result1}입니다.')

print('-'*50)

print('남탕에 입장가능?')
result2 = (gender == '남') or (gender == '여' and age < 3)
print(f'결과는 {result2}입니다.')