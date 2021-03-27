class Personel():
    mesai = '9-18'
    sirket = 'Pycoders'

    def __init__(self, isim, maas, yetenek):

        self.isim = isim
        self.maas = maas
        self.yetenek = yetenek



    def bilgileriGoster(self):
        print("*-" * 20)
        print("Personelin ismi: ", self.isim.upper())
        print("Personelin yetenekleri: ", self.yetenek.upper())
        print("Personelin maaşı: ", self.maas)
        print("*-" * 20)

levent = Personel("levent",5000,"linux,java,pentest")
levent.bilgileriGoster()