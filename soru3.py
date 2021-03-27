class Pycoders:
    
    def __init__(self) -> None:
        
        self.schrijf=self.write
     
    def input(self):
        return input("yaz:").upper()
        
    @property
    def write(self):
        return self.input().upper()
      

        
write=Pycoders()  
print(write.schrijf)
