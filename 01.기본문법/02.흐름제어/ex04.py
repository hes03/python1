#1부터 100까지 합계
sum = 0
for i in range(1, 101):
    sum = sum + i  #sum += i

print(sum)

#짝수
tot = 0
for i in range(2, 101, 2):
    tot += i

print(tot)

#홀수
odd = 0
for i in range(1, 100, 2):
    odd += i
print(odd)

print(tot + odd)

