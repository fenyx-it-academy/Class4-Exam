# Giriş ile girilen bir cumledeki sayilarin ve harflerin miktarini hesaplayan bir irsali yaziniz.
# Ornek girişi: merhaba dünya! 123
# Çıktı:
# HARFLER: 10
# SAYILAR: 3

print("Enter a random sentence: ")
sentence = input()

letters_digits = {"Letters": 0, "Digits": 0}

for x in sentence:
    if x.isalpha():
        letters_digits["Letters"] += 1
    elif x.isdigit():
        letters_digits["Digits"] += 1
    else:
        pass

print("Letters", letters_digits["Letters"])
print("Digits", letters_digits["Digits"])