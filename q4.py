# Input ile alinan bir stringi, harfleri tekrar etmeyecek sekilde ve alfabetik olarak siralayan bir fonksiyon olusturun.
# Boslugu da dikkate alin.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ' cfghilmnoprstuy'

# Ayni inputu tersten siralayip bir liste haline ceviren bir fonksiyon olusturun.
# Ornek input: 'monty pythons flying circus'
# Ornek output: ['circus', 'flying', 'pythons', 'monty']


def sortAlphabetic():
    entry = input("Enter your message:")
    a= (''.join(sorted(entry)))
    x={}

    for i in a:
        x[i] = a.count(i)
    print( "".join(x) )


def printReverse():
    entry = input("Enter your message:")
    entrylist = [i for i in (entry.split(" "))]
    print(entrylist)
    print(entrylist[::-1])

sortAlphabetic()
printReverse()
