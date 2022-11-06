import time
cnt=0
dict={
    1:1,
    2:2
}
def Fibo(n):
    n=int(n)
    global cnt
    cnt+=1
    if n in dict:
        return dict[n]
    else:
        output=Fibo(n-1)+Fibo(n-2)
        dict[n]=output
        return output
    
now=time.time()
a=input("n을 입력하시오 :")
result=Fibo(a)
now-=time.time()

print(f"result: {result}\ncnt: {cnt}\ntime: {-now}")