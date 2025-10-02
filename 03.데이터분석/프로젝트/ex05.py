import os
import pandas as pd

file_score = 'data/학생성적.csv'
file_info = 'data/학생정보.csv'

def inputNum(title):
    while True:
        num = input(title)
        if num == '':
            return ''
        elif not num.isnumeric():
            print('점수는 숫자로 입력하세요')
        else:
            return int(num)

def submenu():
    while True:
        score = pd.read_csv(file_score, index_col='지원번호')
        info = pd.read_csv(file_info, index_col='지원번호')
        df = info.join(score)
        df['총점'] = df.apply(lambda x: sum(x['국어':'사회']), axis=1)
        df['평균'] = df['총점'] / 5

        df.fillna(0, inplace=True)
        cols = ['국어', '영어', '수학', '과학', '사회']

        os.system('cls')

        print('-' * 45)
        print('**************** 성적관리 *******************')
        print('-' * 45)
        print('1.등록|2.목록|3.검색|4.삭제|5.수정|0.종료')
        print('-' * 45)

        menu = input('메뉴선택>')
        if menu == '0':
            print('프로그램 종료')
            break

        elif menu == '1':
            no = inputNum('지원번호>')
            if not no in info.index:
                print('등록되지 않은 번호입니다.')
            elif no in score.index:
                print('성적이 이미 등록되었습니다.')
            else:
                row = info.loc[no]
                print(f'이름:{row["이름"]}')
                grade = []
                for col in cols:
                    num = inputNum(f'{col}>')
                    if num == '': num = 0
                    grade.append(num)
                score.loc[no] = grade
                score.to_csv(file_score)
                print('등록완료!')

            input('아무키나 누르세요')
        
        elif menu == '2':
            while True:
                sel = inputNum('1.최신입력순|2.이름순|3.성적순|>')
                if sel == '':break
                elif sel == 1: df = df.sort_index(ascending=False)
                elif sel == 2: df = df.sort_values('이름')
                elif sel == 3: df = df.sort_values('평균', ascending=False)

                for idx in df.head().index:
                    row = df.loc[idx]
                    print(f'지원번호:{idx:02d}', end=' ')
                    print(f'이름:{row["이름"]}', end=' ')
                    print(f'학교:{row["학교"]}')
                    for col in cols:
                        print(f'{col}:{row[col]:.0f}', end=' ')
                    print(f'평균:{row["평균"]:.2f}')

                    print('-'*60)
                print()
            input('아무키나 누르세요')
        
        elif menu == '3':
            while True:
                sel = inputNum('|1.지원번호|2.학교|3.이름|>')
                if sel == '':
                    break

                elif sel == 1:
                    no = inputNum('지원번호>')
                    if not no in df.index:
                        print('해당 번호가 없습니다.')
                    else:
                        row = df.loc[no]
                        print(f'지원번호:{no}  이름:{row["이름"]}  학교:{row["학교"]}  평균:{row["평균"]:.2f}')
                        print()

                elif sel == 2:
                    word = input('검색어>')
                    filt = df['학교'].str.contains(word)
                    if len(df[filt].index) == 0:
                        print('검색내용이 없습니다.')
                        continue
                    for idx in df[filt].index:
                        row = df.loc[idx]
                        print(f'지원번호:{idx}  이름:{row["이름"]}  학교:{row["학교"]}  평균:{row["평균"]:.2f}')
                    print()

                elif sel == 3:
                    word = input('검색어>')
                    filt = df['이름'].str.contains(word)
                    if len(df[filt].index) == 0:
                        print('검색내용이 없습니다.')
                        continue
                    for idx in df[filt].index:
                        row = df.loc[idx]
                        print(f'지원번호:{idx}  이름:{row["이름"]}  학교:{row["학교"]}  평균:{row["평균"]:.2f}')
                    print()

            input('아무키나 누르세요')
        
        elif menu == '4':
            no = inputNum('지원번호>')
            if not no in info.index:
                print('등록된 번호가 없습니다.')
            elif not no in score.index:
                print('등록된 성적이 없습니다.')
            else:
                row = df.loc[no]
                print(f'이름:{row["이름"]}')
                for col in cols:
                    print(f'{col}:{row[col]}')
                sel = input('삭제하시겠습니까(Y)>')
                if sel == 'Y' or sel == 'y':
                    score.drop(index=no, inplace=True)
                    score.to_csv(file_score)
                    print('삭제성공!')
                
            input('아무키나 누르세요')
        
        elif menu == '5':
            no = inputNum('지원번호>')
            if not no in info.index:
                print('등록된 번호가 없습니다.')
            elif not no in score.index:
                print('등록된 성적이 없습니다.')
            else:
                row = score.loc[no]
                print(f'이름:{info.loc[no, "이름"]}')
                grade = []
                for col in cols:
                    num = inputNum(f'{col}:{row[col]}>')
                    if num == '': 
                        num = row[col]
                    grade.append(num)
                sel = input('수정하시겠습니까(Y)>')
                if sel == "Y" or sel == 'y':
                    score.loc[no] = grade
                    score.to_csv(file_score)
                    print("수정완료!")
            input('아무키나 누르세요')
        
        else:
            print('0~5번을 입력하세요.')

if __name__=='__main__':
    submenu()