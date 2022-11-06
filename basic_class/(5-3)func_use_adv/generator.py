#제네레이터(generator)는 이터레이터(iterator)를 직접 만들 때 사용하는 코드입니다.
#함수 내부에 yield키워드를 사용하면 해당 함수는 제네레이터 함수입니다.
#제네레이터 객체는 next()함수를 통해 함수 내부의 코드를 실행합니다.
#이때 yield 키워드 부분까지만 실행 됌. next()함수의 리턴값으로 yield 키워드 뒤의 값 출력


def test():
    print("A line pass")
    yield 1
    print("B line pass")
    yield 2
    print("C line pass")


#함수를 호출합니다.
output = test()
print("D line pass")
a = next(output)
print(a)
print("E line pass")
b = next(output)
print(b)
print("F line pass")
c = next(output)
print(c)
#한번 더 실행하기
next(output)
