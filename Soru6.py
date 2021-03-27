# hesap.py dosyasindaki islemler ve bakiye degerlerini import edin
# islemler listesini okuyup sirasiyla islem tipi ve miktarina gore 
# hesaptaki tutari guncelleyen bir kod yazin. her bir adimi, 
# olusturdugunuz 'islemler.txt' dosyasina yeni birer satir olarak ekleyin. 
# orn. islem tipi para cekme, tutar=100 => txt dosyasinda
# gorunmesi gereken satir + 100 eger islem tipi para cekme ise ve cekilmek 
# istenen miktar halihazirda hesapta olan bakiyeden fazla ise, raise 
# kullanarak exception olusturun ve "hesapta yeterli miktar yoktur"
# benzeri bir hata mesaji printleyin. en son adimda hesaptaki guncel 
# tutari txt dosyasina yazin (bakiye: miktar) seklinde.
# tum bu akisi dosya acma/kapama islemleri ve try-except yontemi ile yapin.

# tum kod neticesinde olusturmaniz gereken islemler.txt dosyasinin icerigi 
# asagidaki gibi olmalidir:
# + 100
# + 200
# - 50
# + 100
# - 250
# + 30
# bakiye: 130

# tum kod neticesinde terminalde gorunmesi gereken degerler:
# hesapta yeterli bakiye yoktur
# bakiye: 130

from hesap import bakiye, islemler

class Hesap:
    def __init__(self, balance):
        self.balance = balance
        self.operations = list()

    def deposit(self, value):
        self.balance += value
        self.operations.append(('+', value))

    def withdraw(self, value):
        if(self.balance >= value):
            self.balance -= value
            self.operations.append(('-', value))
        else:
            raise("hesapta yeterli miktar yoktur")
    
    def save(self):
        of = open("islemler.txt", 'w')
        for o in self.operations:
            of.write(f"{o[0]} {o[1]}\n")



my_hesap = Hesap(bakiye)

for islem in islemler:
    ot = islem["islem_tipi"]
    ov = islem["miktar"]
    if ot == "para_yatirma":
        my_hesap.deposit(ov)
    else:
        try:
            my_hesap.withdraw(ov)
        except :
            print(f"Error can not withdraw {ov}")

my_hesap.save()