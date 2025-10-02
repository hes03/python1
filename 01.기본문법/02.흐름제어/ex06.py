no = int(input('학생수>'))
names = []
for i in range(no):
    name = input('이름>')
    names.append(name) #names = names + list(name) 

print(names)

for i in range(len(names)):
    print(names[i], end=',')

print('\n')

for name in names:
    print(name)

print('\n')

for i, name in enumerate(names):
    print(i, name, end=',')
