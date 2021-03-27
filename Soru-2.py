# Kullanıcı tarafindan girilen n sayisi kadar elemani olan ve elemanları arasinda (i:i*i) iliskisi olan bir sozluk olusturunuz.
# Ornek girişi: 8
# Çıkış: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

n=int(input("Input a number: "))
a = dict()

for i in range(1,n+1):
    a[i]=i*i

print(a)