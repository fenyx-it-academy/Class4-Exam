
# Input ile alinan bir stringi, harfleri tekrar etmeyecek sekilde ve alfabetik olarak siralayan bir fonksiyon olusturun. Boslugu da dikkate alin.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ' cfghilmnoprstuy'

# Ayni inputu tersten siralayip bir liste haline ceviren bir fonksiyon olusturun.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ['circus', 'flying', 'pythons', 'monty']

s=input("string giriniz:").split(" ")   

def myFirst():     
    t=set()
    for i in s:
        t.update(i)
    t=list(t)
    t.sort()
    print("".join(t))

def myReverse():    
    s.sort()
    print(s)
    
    
myFirst()
myReverse()