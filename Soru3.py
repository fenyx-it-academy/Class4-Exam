# En az iki metodu olan bir Class olusturunuz.
# 1.metot =>  inputAl: Kullanicidan input alma.
# 2.metot =>  yazdir: Alinan inputu terminale buyuk harflerle yazdirma metodu.
class soru3:
    def inputAl(self):
        self.x=input('yazi giriniz:  ')
        return self.x

    def yazdir(self):
        self.x=self.x.upper()
        print(self.x)

a=soru3()
a.inputAl()
a.yazdir()