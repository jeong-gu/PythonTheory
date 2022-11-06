#조건문으로 예외처리 - 기본 예외 처리
pi = 3.141592
while 1:
    input_a = input("정수를 입력하시오 : ")

    if input_a.isdigit():
        input_a = int(input_a)
        print("원의 반지름은 : {:.2f}".format(2 * pi * input_a))
        print("원의 넓이는 : {:.2f}".format(pi * input_a * input_a))
        break
    else:
        print("------정수만 입력하십시오-----\n")
