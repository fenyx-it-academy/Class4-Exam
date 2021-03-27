# Input ile girilen bir cumledeki sayilarin ve harflerin miktarini hesaplayan bir fonksiyon yaziniz.
# Ornek input: hello world! 123
# Output:
# HARFLER: 10
# SAYILAR: 3

metin = input('metín giriniz: ')
sayi=0
harf=0
for i in metin:
    if i.isalpha():
        harf+=1
    elif i.isnumeric():
        sayi+=1
print("HARFLER: {}\nSAYILAR: {}".format(harf,sayi))
