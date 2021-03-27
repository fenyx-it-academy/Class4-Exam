# 2000 ve 3200 sayilari arasinda (2000 ve 3200 dahil) 7'ye tam bolunebilen fakat 5'in kati olmayan tum sayilari 
# aralarinda virgul olacak sekilde tek satirda terminale bastirin.

for i in range(2000,3201):
    if i % 7 == 0 and not i % 5 == 0:
        print(i, end=",")