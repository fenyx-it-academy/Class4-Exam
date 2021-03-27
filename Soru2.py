# Kullanici tarafindan girilen n sayisi kadar elemani olan ve elemanlari arasinda (i:i*i) iliskisi bulunan bir 
# sozluk olusturunuz.
# Ornek input: 8
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n = int(input("Eleman sayisini giriniz: "))

dict1 = dict()

for i in range(n):
    dict1[i+1] = (i+1) * (i+1)

print(dict1)