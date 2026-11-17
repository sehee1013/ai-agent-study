from dataclasses import dataclass

@dataclass
class BookInfo:
    title : str
    author : str
    publisher : str

# PhysicalBook 클래스 정의
@dataclass
class PhysicalBook(BookInfo):
    weight : float
    size : str

# EBook 클래스 정의
@dataclass
class EBook(BookInfo):
    format_type : str
    download_url : str

physical_book = PhysicalBook(
    title="파이썬 클래스 톺아보기",
    author="라이캣",
    publisher="위니버시티",
    weight=0.780,  # kg
    size="188*240*35"  # mm
)

digital_book = EBook(
    title="JavaScript 베이스캠프",
    author="빙키",
    publisher="위니버시티",
    format_type="EPUB",
    download_url="https://example.com/download"
)

print(physical_book.title)  # 파이썬 클래스 톺아보기
print(physical_book.weight)  # 0.780
print(physical_book.size)   # 188*240*35

print(digital_book.title)  # JavaScript 베이스캠프
print(digital_book.format_type)  # EPUB
print(digital_book.download_url)  # https://example.com/download