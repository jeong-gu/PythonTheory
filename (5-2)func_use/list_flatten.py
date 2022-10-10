list_a=[[1,2,3],[4,[5,6]],7,[8,9]]
result=[]
def flatten(element):
    global result
    if type(element)==list:
        for i in element:
            flatten(i)
    else:
        result.append(element)

flatten(list_a)
print(result)