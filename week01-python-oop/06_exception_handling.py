# 숫자 입력 받기
value = input()

try:
    # 입력받은 값을 int()로 정수 변환
    value = int(value)
    # 성공하면 "입력하신 숫자는{value}입니다" 형식으로 출력
    print(f"입력하신 숫자는 {value}입니다.")
except ValueError:
    # 정수로 변환할 수 없는 입력에 대한 예외 처리
    print("숫자만 입력해주세요.")

# 완료 메시지 출력
print("입력 처리 완료")