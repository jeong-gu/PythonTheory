#예외 객체

try:
    num_input = int(input("정수를 입력하시오 : "))
    print(num_input, "이 정상적으로 입력되었습니다.")

except Exception as exception:
    print("정수가 입력되지 않았습니다.")
    print("type: ", type(exception))
    print("exception: ", exception)
