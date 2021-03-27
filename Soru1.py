sayi1 = 2000
sayi2= 3200
list =[]

for sayi in range(sayi1, sayi2+1):
    if (sayi % 7 == 0 and sayi % 5 != 0):
        list.append(sayi)
print(list)