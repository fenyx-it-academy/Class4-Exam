a = input("Lütfen bir cümle giriniz:")
d=l=0
for c in a:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Harfler", l)
print("Sayılar", d)