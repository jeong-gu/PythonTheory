#기본 자료형 함수
def func1(b):
    b = 20


a = 10
print(a)
func1(a)
print(a)
print()


#---------------------------
#객체 자료형 함수
def func2(k):
    k.append(4)


j = [1, 2, 3]
print(j)
func2(j)  #reference 참조
print(j)
print()

#매개변수는 변수자체가 불러지는 것이 아니라, 값만 전달되는 것이다.
# a:10, b:10   //// j:0x01... k:0x01...


def object_change(y):
    y = [4, 5, 6]
    print("\nafter: \ny: ", y)


x = [1, 2, 3]
print("x: ", x)
object_change(x)
print("x: ", x)
