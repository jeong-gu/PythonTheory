#예외를 처리할 수 있는 구문
#프로그램이 죽지않도록
#try_except
pi = 3.141592
while 1:
    try:  #예외가 발생할 수 있는 부분
        number_a = int(input("정수를 입력해주세요 : "))  #예외가 발생할 수 있는 코드
        print("원의 반지름은 : {:.2f}".format(2 * pi * number_a))
        print("원의 넓이는 : {:.2f}".format(pi * number_a * number_a))
        break
    except:  #예외가 발생했을떄 실행
        print("----뭔가 잘못됐음-----\n\n")
    #except:      #귀찮아서 종료되는 것만 막고자할 때 pass로 그냥 처리
    #pass
