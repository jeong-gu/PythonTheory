import time
cnt=0
def Fibo(n):
    n=int(n)
    global cnt
    cnt+=1
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return Fibo(n-1)+Fibo(n-2)

now=time.time()
a=input("n을 입력하시오 :")
result=Fibo(a)
now-=time.time()

print(f"result: {result}\ncnt: {cnt}\ntime: {-now}")