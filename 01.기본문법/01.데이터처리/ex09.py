#기본함수
print(1, abs(-3)) #절대값
print(2, pow(4, 2))  #제곱수 4^2
print(3, max(5, 2, 10, 1, 9)) #최대값
print(4, min(5, 2, 10 , 1, 9)) #최소값
print(5, round(3.14)) #반올림
print(6, round(3.14159, 3)) #셋째자리까지 출력

from math import * 
print(7, floor(4.99)) #내림
print(8, ceil(3.14))  #올림
print(9, sqrt(16))  #제곱근

from random import *
print(10, random())  # 0 이상 1 미만
print(11, random() * 10)  # 0 이상 10 미만
print(11, int(random() * 10))  #0~9
print(12, randint(1, 45))  #1~45