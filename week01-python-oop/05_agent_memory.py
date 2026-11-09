# AgentMemory 클래스 정의
class AgentMemory:
    # 대화 기록 리스트를 인스턴스 변수로 저장
    def __init__(self, msg_list):
        self.msg_list = msg_list

    # 저장된 대화 기록의 개수 반환
    def __len__(self):
        return len(self.msg_list)
    
    # 인덱스에 해당하는 대화 기록 반환
    def __getitem__(self, key):
        return self.msg_list[key]
    
    # 대화 기록을 순회할 수 있는 반복자 반환
    def __iter__(self):
        return iter(self.msg_list)

# 결과 출력
memory = AgentMemory([
    "안녕하세요", 
    "python을 공부하고 있어요", 
    "AI Agent를 만들고 싶어요"
])

print(len(memory))
print(memory[0])

for item in memory:
    print(item)