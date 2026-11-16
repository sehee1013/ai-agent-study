# Book 클래스 생성
class Book:
    # ISBN, 도서명, 저자, 가격, 재고 정보 인스턴스 변수로 초기화
    def __init__(self, isbn, title, author, price, stock):
        self.__isbn = isbn      # ISBN는 비공개 속성으로 생성
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    # 가격과 재고는 음수 입력 시 ValueError
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("가격은 음수가 될 수 없습니다.")
        self._price = value

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("재고는 음수가 될 수 없습니다.")
        self._stock = value
    
    
    # 책 정보 출력 문자열 메소드 정의
    def __str__(self):
        return f"<{self.title}> 저자: {self.author}, 가격: {self.price}원, 재고: {self.stock}권"
    # ISBN 같으면 True, 다르면 False
    def __eq__(self, other):
        return self.__isbn == other.__isbn
    # 가격이 더 작으면 True, 아니면 False
    def __lt__(self, other):
        return self.price < other.price


book1 = Book("123-4-56-789012-3", "파이썬 클래스 톺아보기", "라이캣", 25000, 10)
book2 = Book("123-4-56-789012-4", "JavaScript 베이스캠프", "빙키", 15000, 5)

try:
    print(book1.price)  # 25000
    book1.price = -5000  # 음수 price 설정 시도(에러발생)
except ValueError as e:
    print(e)

print(book1.price)  # 25000 (음수가 되지 않음)

try:
    print(book1.stock)  # 10
    book1.stock = -3  # 음수 stock 설정 시도(에러발생)
except ValueError as e:
    print(e)

print(book1.stock)  # 10 (음수가 되지 않음)

print(book1)  # <파이썬 클래스 톺아보기> 저자: 라이캣, 가격: 25000원, 재고: 10권
print(book1 == book2)  # False
print(book1 < book2)  # False