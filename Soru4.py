# Input ile alinan bir stringi, harfleri tekrar etmeyecek sekilde ve alfabetik olarak siralayan bir fonksiyon olusturun.
# Boslugu da dikkate alin.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ' cfghilmnoprstuy'

# Ayni inputu tersten siralayip bir liste haline ceviren bir fonksiyon olusturun.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ['circus', 'flying', 'pythons', 'monty']

# x=input('bir yazi giriniz:')
metin='monty pythons flying circus'
x=list(metin)
y = sorted(set(x))
print(y)
#########################################
z=metin.split(" ")
t=z[::-1]
print(t)
