min=2  #앉힐수있는최소사람수
max=10 #앉힐수있는최대사람수
number =int(input("사람 수를 입력하시오 : "))
#전체 사람 수

dic = {}

def quiz1(remain,num): # remain : 남은 사람 수, num: 앉힌 사람 수
    key = str([remain,num])
    if key in dic:
        return dic[key]
    if remain<0:
        return 0
    if remain == 0:
        return 1
    
    cnt=0
    for i in range(num,max+1):
       cnt+=quiz1(remain-i,i)
    dic[key]=cnt
    return cnt

print(quiz1(number,min))
            

        