#딕셔너리
students = {1:'홍길동', 2:'심청이', 3:'강감찬'}
print(students, type(students))
print(students.get(2))
print(students[2])

students[4] = '박명수'
print(students, type(students))
students[2] = '박명수' 
print(students)

print('심청이' in students)
print('박명수' in students)
print(3 in students)

keys = students.keys()
print(keys, type(keys))
values = students.values()
print(values, type(values))

print('박명수' in values)
