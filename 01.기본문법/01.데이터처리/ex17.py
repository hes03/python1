#집합(set)
java = {'유재석', '홍길동', '심청이'}
print(java, type(java))

python = {'심청이', '강호동', '이순신'}
print(2, python, type(python))

print(3, java.intersection(python)) #교집합
print(4, java.union(python)) #합집합
print(5, java.difference(python))
print(6, python.difference(java))

java.add('강호동') #추가
print(7, java)
java.remove('유재석') #삭제
print(8, java)

java = list(java)
print(9, java, type(java))

java = tuple(java)
print(10, java, type(java))

java = set(java)
print(11, java, type(java))
