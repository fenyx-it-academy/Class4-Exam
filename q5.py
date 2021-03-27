
# Input ile girilen bir cumledeki sayilarin ve harflerin miktarini hesaplayan bir fonksiyon yaziniz.
# Ornek input: hello world! 123
# Output:
# HARFLER: 10
# SAYILAR: 3

s=input("string ve sayi giriniz:").split(" ")
harfler=0
sayilar=0
for i in s:    
    if i.isdigit():
        sayilar += len(i)        
    else:        
        harfler += len(i)
print('HARFLER:',harfler)
print('SAYILAR:',sayilar)       