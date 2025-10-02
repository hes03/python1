num1 = input('숫자1>')
num2 = input('숫자2>')
num1 = int(num1)
num2 = int(num2)
add = num1 + num2
# add = int(num1) + int(num2)
# 산술연산자
print(f'{num1}+{num2}={add}')
print(f'{num1}-{num2}={num1-num2}')
print(f'{num1}*{num2}={num1*num2}')
print(f'{num1}/{num2}={num1/num2:.2f}')
print(f'{num1}%{num2}={num1%num2}')  #나머지
print(f'{num1}//{num2}={num1//num2}')  #몫