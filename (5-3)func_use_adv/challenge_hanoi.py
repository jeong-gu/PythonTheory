# 도전문제 - 하노이 탑
dict = {}  #hanoi() 리턴 값 저장


def hanoi_trace(n, start, mid, end):
    if n == 1:
        print("{}탑 -> {}탑".format(start, end))
    else:
        hanoi_trace(n - 1, start, end, mid)
        print("{}탑 -> {}탑".format(start, end))
        hanoi_trace(n - 1, mid, end, start)


def hanoi(n):
    if n == 1:
        return 1
    if n not in dict:
        dict[n] = hanoi(n - 1) + 1 + hanoi(n - 1)
    return dict[n]


num = int(input("원판의 개수를 입력하세요: "))
hanoi_trace(num, "A", "B", "C")
result = hanoi(num)

print(result)
