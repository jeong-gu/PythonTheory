#파일을 엽니다.

file=open("basic.txt","w")
file.write("Hello, Hon-gong-pa\nThis is 'basic.txt'\n")
file.close()

#with 키워드를 사용합니다. 위와 동일한 코드임.

with open("next.txt","w") as file:
    file.write("Hello, Hon-gong-pa\nThis is 'next.txt'\n")