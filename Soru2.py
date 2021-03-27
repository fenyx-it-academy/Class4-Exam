indeks=int(input('indeks giriniz: '))
anahtarlar= list(range(1,indeks+1))
degerler = list()
for kareal in anahtarlar:
    degerler.append(kareal**2)
sozluk = dict(zip(anahtarlar,degerler))
print(sozluk)