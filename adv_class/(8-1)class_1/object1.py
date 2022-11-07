#객체 만들어보기
from random import uniform


def create_student(name, kor, math, eng, science):
    return {
        "name": name,
        "kor": int(kor),
        "math": int(math),
        "eng": int(eng),
        "science": int(science)
    }


def get_sum(student):
    sum = 0
    for key in student:
        if (key == "name"):
            continue
        sum += student[key]
    return sum


def get_avg(student):
    return get_sum(student) / 4


def get_info(student):
    print(f'{student["name"]}\t{get_sum(student)}\t{get_avg(student)}')


def get_ran():
    return uniform(50, 100)


students = [
    create_student("A", get_ran(), get_ran(), get_ran(), get_ran()),
    create_student("B", get_ran(), get_ran(), get_ran(), get_ran()),
    create_student("C", get_ran(), get_ran(), get_ran(), get_ran()),
    create_student("D", get_ran(), get_ran(), get_ran(), get_ran()),
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    get_info(student)

print("-----------------------------------")
