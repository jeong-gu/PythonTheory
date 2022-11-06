import os

print("현재의 운영체제: ", os.name)
print("현재 폴더.: ", os.getcwd())
print("현재 폴더 내부 요소: ", os.listdir())

with open("test.txt", "w") as file:
    file.write("HI HI hello")

os.rename("test.txt", "new.txt")

os.remove("new.txt")
#os.unlink("new.txt")

os.system("dir")
