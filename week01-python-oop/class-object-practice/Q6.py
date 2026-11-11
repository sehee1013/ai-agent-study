# 첫 줄: 학생 수 n. 이어지는 n 줄: "이름 점수" (예: "kim 95" -> ["kim", "95"])
n = int(input())
rows = [input().split() for _ in range(n)]

# Student 클래스 정의
class Student:
    """
    학생 이름과 성적을 입력 받아 등급을 출력하기
    """
    # 이름, 점수 정보를 입력 받아 인스턴스 변수 선언
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 성적 등급 판별 
    def grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        return "F"  

# ---- 호출부 (수정 금지) ----
for name, score in rows:
    s = Student(name, int(score))
    print(f"{s.name} {s.score} {s.grade()}")