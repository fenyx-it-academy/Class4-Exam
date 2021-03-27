
n =int( input('Bir sayi giriniz:'))

listem = [x**1 for x in range (1,n+1)]
listem2= [x**2 for x in range (1,n+1)]
print('sayilar:',listem)
print('katlari:',listem2)
def list_to_dict(param1,param2):
    return dict(list(zip(param1,param2)))
    list_to_dict(listem,listem2)
f=lambda x,y: dict(list(zip(x,y)))
print('sozluk:',f(listem,listem2))

