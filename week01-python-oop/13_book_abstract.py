from abc import ABC, abstractmethod
from enum import Enum

# BookFormat 클래스 생성
class BookFormat(Enum):
    PAPER = "종이책"
    EBOOK = "전자책"
    AUDIO = "오디오북"

class Book(ABC):
    # ISBN, 도서명, 저자, 가격, 재고 정보 인스턴스 변수로 초기화
    def __init__(self, isbn, title, author, price, stock):
        self.__isbn = isbn      # ISBN는 비공개 속성으로 생성
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
    # 할인가 계산하는 추상화 메소드 정의
    @abstractmethod
    def calculate_discount(self):
        pass

# Book 클래스를 상속 받는 종이책 클래스 정의
class PaperBook(Book):
    def calculate_discount(self):
        return int(self.price * 0.9)
# Book 클래스를 상속 받는 전자책 클래스 정의
class EBook(Book):
    def calculate_discount(self):
        return int(self.price * 0.8)
# Book 클래스를 상속 받는 오디오북 클래스 정의
class AudioBook(Book):
    def calculate_discount(self):
        return int(self.price * 0.85)

paper_book = PaperBook("123-4-56-789012-3", "파이썬 클래스 톺아보기", "라이캣", 25000, 10)
ebook = EBook("123-4-56-789012-4", "JavaScript 베이스캠프", "빙키", 15000, 5)
audio_book = AudioBook("123-4-56-789012-5", "Python 베이스캠프", "뮤라", 12000, 50)

print(paper_book.calculate_discount())  # 22500 (10% 할인)
print(ebook.calculate_discount())      # 12000 (20% 할인)
print(audio_book.calculate_discount()) # 10200 (15% 할인)