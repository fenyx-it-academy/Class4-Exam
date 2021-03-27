# 2000 ve 3200 sayilari arasinda (2000 ve 3200 dahil) 7'ye tam bolunebilen 5'in kati olmayan tum sayilari
# aralarinda virgul olan sekilde tek hicivda terminale bastirin.
import math
sayi_list = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        sayi_list.append(i)
        print(sayi_list)
