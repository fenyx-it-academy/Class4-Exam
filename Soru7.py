# "Yazici Ciftligi" adını verdiğiniz milyon dolarlık bir is fikrine sahipsiniz.
# Pek çok insanın ofislerinde ve evlerinde yazıcı kullandığını biliyorsunuz ve 
# bunun hiç mantıklı olmadigini dusunuyorsunuz.
# Neden tüm yazıcıları yazıcı çiftliğinizde birleştirip, kullanıcıların 
# yazicilarinizi kullanarak dosyalar yazdirmasini saglayip,
# bu dosyaları postayla onlara göndermeyesiniz ki?
# Elbette bu harika bir fikir, bu yüzden hemen başlamaya karar veriyorsunuz.
# Ana sorun, sunucuza gelen binlerce yazdırma komutunu işlemek ve bunları sahip 
# olduğunuz 64 yazıcıya tek tek göndermek.
# Amaç, herhangi bir baskı talebini aldıktan sonra 1 saat içinde baskiyi 
# tamamlamak ve göndermek.
# Hizmetinizin kullanıcı sayısının hızla artacağını tahmin ediyorsunuz, bu 
# nedenle işiniz büyüdükçe taleple başa çıkmak için
# yeni sunucular ve yazıcılar ekleyebilmeniz gerek.
# Kullanmanız gereken veri yapıları, bu veri yapilarinin nasil uygulamaya 
# dokulecegi ve baskı hizmetini
# etkin bir şekilde çalıştırmak için gerekli olacak algoritmalar hakkında
#  yaklasik 10 cümle ile kısa bir paragraf yazın.
# Seçimlerinizi çalışma süresi ve depolama boyutu açısından açıklayın. 
# (Time & Space Complexity)



# 1- Talep class olustururum
# 2- Yazici class olustururum
# 3- Job class olustururum
# 4- Job => talep, yazici
# 5- talep => tahmini sure, aders vs
# 6- yazici => hiz, renk vs
# 7- Main => FIFO queue
# 8- Main de Gelen talep FIFO olarak takip eden bir yapi olusturarak
# 9- Her yazicilarin durumunu anlik takip eden bir queue kullanarak,
# 10- Her talebe ilk yazici bosaldigi anda yada bos bir yazici var ise 
#     bur Job objesi olusturup aktip olan joblar listesine eklerim.
# 11- Bu yapida eklenen isler surekli bir yaziciya verilecektir. Islem
#     tamamlandiginda is objesi yaziciyi bosa cikarir ve talep i tamamlandi diye isaretler.
# 12- Yeni yazici eklenmesi durumunda yapilmasi gerelen sadece yazicilar listesine 
#     o yaziciyi eklemek olacaktir. Bozulan yazici olsa da ayni durum gecerli.