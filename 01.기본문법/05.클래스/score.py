from student import Student

class Score(Student):
    def __init__(self): #성적 객체를 생성하는 생성자
        super().__init__()
        self.kor = 0
        self.eng = 0
        self.mat = 0

    def info_print(self): #성적 객체의 정보를 출력하는 메서드
        super().info_print()
        print(f'국어:{self.kor}, 영어:{self.eng}, 수학{self.mat}')

    def result(self):  #결과 구하는 메서드
        avg = (self.kor + self.eng + self.mat) / 3
        if avg < 70:
            return 'FAIL'
        else:
            return "PASS"

    def dict(self):  #딕셔너리로 변환하는 메서드
        return {'no':self.no, 'name':self.name, 
                'kor':self.kor, 'eng':self.eng, 'mat':self.mat, 
                'avg':(self.kor + self.eng + self.mat) / 3, 
                'result':self.result()}
    

if __name__ =='__main__':
    s = Score()
    s.no = '01'
    s.name = '홍길동'
    s.kor = 90
    s.eng = 90
    s.mat = 90

    s.info_print()
    print(s.dict())