#랜덤한 숫자를 가져오기 위해 가져옵니다.
import random
#간단한 한글 리스트
ran_hanguls=list("가나다라마바사아자차카타파하")
with open("info.txt","w") as file:
    for i in range(100):   #100명의 랜덤 데이터 
        name=random.choice(ran_hanguls)+random.choice(ran_hanguls)
        weight=random.randrange(40,100)
        height=random.randrange(140,190)
        file.write(f"{name}, {height}, {weight}\n")

