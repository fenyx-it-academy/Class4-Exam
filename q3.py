
# En az iki metodu olan bir Class olusturunuz.
# 1.metot =>  inputAl: Kullanicidan input alma.
# 2.metot =>  yazdir: Alinan inputu terminale buyuk harflerle yazdirma metodu.

class EnAz2Method:
    def __init__(self,q=None):
        self.q=q        
                
    def method1(self):
        self.q=input('bir isim giriniz:')
        self.method2()       
        
    def method2(self):
        result=self.q
        print(result.upper())

c=EnAz2Method()

c.method1()