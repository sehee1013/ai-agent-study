# 첫 줄: 도서 수 n. 이어지는 n 줄: "제목 저자 쪽수" (예: "파이썬 김철수 250" -> ["파이썬", "김철수", "250"])
n = int(input())
rows = [input().split() for _ in range(n)]

# Book 클래스를 정의
class Book:
    """도서 정보를 저장하는 클래스"""

    # 타이틀, 이름, 페이지(정수) 입력 받기
    def __init__(self, title, author, pages=int):
        self.title = title
        self.author = author
        self.pages = pages
    
    def describe(self):
        return f"{self.title} - {self.author} ({self.pages}쪽)"
    
    def is_long(self):
        return self.pages >= 300

# ---- 호출부 (수정 금지) ----
for title, author, pages in rows:
    book = Book(title, author, int(pages))
    print(book.describe())
    print(book.is_long())