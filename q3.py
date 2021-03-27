# En az iki metodu olan bir Class olusturunuz.
# 1.metot =>  inputAl: Kullanicidan input alma.
# 2.metot =>  yazdir: Alinan inputu terminale buyuk harflerle yazdirma metodu.


class Yazdir:


    def inputAl(self):
        entry = input("enter your input: ")
        self.entry = entry

    def yazdir(self):
        print(self.entry.upper())

a=Yazdir ()
a.inputAl()
a.yazdir()