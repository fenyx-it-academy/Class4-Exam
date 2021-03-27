# En az iki metodu olan bir Class olusturunuz.
# 1.metot =>  inputAl: Kullanicidan input alma.
# 2.metot =>  yazdir: Alinan inputu terminale buyuk harflerle yazdirma metodu.

class Myclass:

    def inputAl(self):
        a = input("Lutfen en sevdiginiz harfi girin: ")
        self.value = a

    def yazdir(self):
        print(self.value.upper())

v = Myclass()

v.inputAl()

v.yazdir()

