from dataclasses import dataclass, field

# dataclass 사용하여 정보 저장
@dataclass
# Agent 클래스 정의
class Agent:
    name : str
    role : str = "Assistant"
    tasks : list = field(default_factory=list)

    def __post_init__(self):
        print(f"{self.name} 에이전트 생성 완료")
    def add_task(self, task):
        self.tack = task


search = Agent("Sakura", "Search")
coding = Agent("PythonBot", "Coding")
search.add_task("웹 검색")
coding.add_task("코드 작성")

print(search)
print(coding)