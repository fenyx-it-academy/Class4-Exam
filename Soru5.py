# Input ile girilen bir cumledeki sayilarin ve harflerin miktarini hesaplayan bir fonksiyon yaziniz.
# Ornek input: hello world! 123
# Output:
# HARFLER: 10
# SAYILAR: 3

s = input("Lutfen sayi ve rakamlardan olusn bir metin giriniz: ")

def count(s):

    sayilar = 0
    harfler = 0

    for c in s:
        if c.isalpha():
            harfler += 1
        elif c.isnumeric():
            sayilar += 1

    return sayilar, harfler

s, h = count(s)
print("Sayilar: {}".format(s))
print("Harfler: {}".format(h))
