# Input ile alinan bir stringi, harfleri tekrar etmeyecek sekilde ve alfabetik olarak siralayan bir fonksiyon olusturun. 
# Boslugu da dikkate alin.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ' cfghilmnoprstuy'

# Ayni inputu tersten siralayip bir liste haline ceviren bir fonksiyon olusturun.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ['circus', 'flying', 'pythons', 'monty']

text1 = str(input("Lutfen metni girin: "))

li = text1.split(" ")
li.reverse()
print(li)

h = list(set(text1))
h.sort()
print(''.join(h))