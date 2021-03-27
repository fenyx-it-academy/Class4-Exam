kelime=input('Bir cumle giriniz:')
for i in sorted(kelime):
    print(i, end="")
a=len(kelime)

for i in range(1,a+1):
    b=kelime[a-i]
    print(b,end=" ")