users=input("cumle gir:")
list=[]
#a='monty pythons flying circus'
def sirala(users):
    for i in users:
        if i not in list and i !=" ":
            list.append(i)
    print("".join(sorted(list)))

def hizala(users):
    sira=[i for i in users]    
    sira="".join(sira)
    print(sira[::-1])
    
    
hizala(users)
sirala(users)