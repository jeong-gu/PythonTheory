#파일을 열고, 읽고 출력합니다.

with open("basic.txt","r") as file:
    print(file.read())
    
with open("next.txt","r") as file:
    contents=file.read()
    print(contents)
    