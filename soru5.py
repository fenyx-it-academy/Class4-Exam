users=input("cumle gir:")
#a= 'hello world! 123'
def hesapla(users):    
    l=[i for i in users if i!=" " and i!='!']
    list=[]
    for i in l:
        if i.isdigit() is True:
            list.append(i)
    print(f'HARFLER: {len(l)-len(list)}')
    print(F'SAYILAR: {len(list)}')
    
hesapla(users)