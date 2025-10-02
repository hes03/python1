#숫자가 입력될때까지 계속 입력
def inputNum(title):
    while True:
        num = input(f'{title}')
        if num.isnumeric():
            return int(num)
        elif num == '':
            return num
        else:
            print('숫자로 입력하세요!')


#검색함수(list와 code를 입력받아 list에서 code를 검색)
def search(list, code):
    for index, item in enumerate(list):
        if item['code'] == code:
            return index
        
#메뉴출력함수
def menuPrint(title):
    print(f"\n****************{title}*****************")
    print('--------------------------------------------')
    print("|1.입력|2.검색|3.목록|4.삭제|5.수정|0.종료|")
    print('--------------------------------------------')

#새로운 코드를 생성하는 함수
def newCode(list):
    if len(list) == 0:
        return 1
    
    codes = []
    for s in list:
        codes.append(s['code'])
    max_code = max(codes)
    return max_code + 1

#아이템 출력 함수
def itemPrint(item):
    keys = item.keys()
    for key in keys:
        if isinstance(item[key], int):
            print(f'{item[key]:,}', end='\t')
        else:
            print(item[key], end='\t')
    print('\n-------------------------------')

if __name__ == '__main__': #import해서 실행안됨. 여기에서만 실행  
    sale = [
        {'code':1, 'name':'냉장고', 'price':250, 'qnt':5},
        {'code':2, 'name':'세탁기', 'price':150, 'qnt':3},
    ]

    itemPrint(sale[1])