class StudyAgent:
	# 이름, 공부 횟수 인스턴스 변수로 초기화
	def __init__(self, name, study_count):
		self.name = name
		self.study_count = study_count
	# 문자열 출력 양식 설정
	def __str__(self):
		return f"이름: {self.name} / 공부 횟수: {self.study_count}회"
	# 공부 횟수 기준으로 객체 참/거짓 판단
	def __bool__(self):
		return self.study_count >= 1

# StudyAgent 인스턴스 생성
agent1 = StudyAgent("Sakura", 5)
agent2 = StudyAgent("LazyBot", 0)


print(agent1)
print(agent2)

print(bool(agent1))
print(bool(agent2))

if agent1: 
	print("Sakura는 오늘 공부했습니다.")

if agent2:
	print("LazyBot은 오늘 공부했습니다.")