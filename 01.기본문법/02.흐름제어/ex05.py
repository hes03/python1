names = ['홍길동', '심청이', '강감찬', '이순신']
no = 1
for name in names:
    print(f'{no}:{name}')
    no += 1

print('\n')

for i, name in enumerate(names):
    print(f'{i+1}:{name}')

print('-'*50)

for i in range(len(names)):
    print(f'{i+1}:{names[i]}')

