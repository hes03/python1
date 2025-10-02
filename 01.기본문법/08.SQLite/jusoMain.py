from function import *
from jusoDB import *

while True:
    menuPrint('주소관리')
    menu = input('메뉴선택>')
    if menu == '0':
        print('프로그램을 종료합니다.')
        break

    elif menu == '1': #입력
        p = Person()
        p.name = input('이름>')
        if p.name == '':
            continue
        p.address = input('주소>')
        insert(p)
        p.print() 

    elif menu == '2': #검색
        p = Person()
        value = input('검색어>')
        if value=='': break
        rows = search(value)
        for row in rows:
            p.seq = row[0]
            p.name = row[1]
            p.address = row[2]
            p.print()

    elif menu == '3': #목록
        rows = list()
        for row in rows:
            person = Person()
            person.seq = row[0]
            person.name = row[1]
            person.address = row[2]
            person.print()

    elif menu == '4': #삭제
        p = Person()
        p.seq = int(input('삭제번호>'))
        row = read(p.seq)
        if row == None:
            print('삭제번호가 없습니다.')
        else:
            delete(p.seq)
            print('삭제완료!')


    elif menu == '5': #수정
        p = Person()
        p.seq = int(input('수정번호>'))
        row = read(p.seq)
        if row == None:
            print('수정번호가 없습니다.')
        else:
            p.name = row[1]
            p.address = row[2]
            name = input(f'이름:{p.name}>')
            if name != '':
                p.name = name
            address = input(f'주소:{p.address}>')
            if address != '':
                p.address = address
            update(p)
            print('수정완료!')


    else:
        print('0~5번 숫자를 입력하세요')