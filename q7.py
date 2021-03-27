# "Yazici Ciftligi" adini verdiginiz milyon dolarlik bir is fikrine sahipsiniz.
# Pek �ok insanin ofislerinde ve evlerinde yazici kullandigini biliyorsunuz ve bunun hi� mantikli olmadigini dusunuyorsunuz.
# Neden t�m yazicilari yazici �iftliginizde birlestirip, kullanicilarin yazicilarinizi kullanarak dosyalar yazdirmasini saglayip,
# bu dosyalari postayla onlara g�ndermeyesiniz ki?
# Elbette bu harika bir fikir, bu y�zden hemen baslamaya karar veriyorsunuz.
# Ana sorun, sunucuza gelen binlerce yazdirma komutunu islemek ve bunlari sahip oldugunuz 64 yaziciya tek tek g�ndermek.
# Ama�, herhangi bir baski talebini aldiktan sonra 1 saat i�inde baskiyi tamamlamak ve g�ndermek.
# Hizmetinizin kullanici sayisinin hizla artacagini tahmin ediyorsunuz, bu nedenle isiniz b�y�d�k�e taleple basa �ikmak i�in
# yeni sunucular ve yazicilar ekleyebilmeniz gerek.
# Kullanmaniz gereken veri yapilari, bu veri yapilarinin nasil uygulamaya dokulecegi ve baski hizmetini
# etkin bir sekilde �alistirmak i�in gerekli olacak algoritmalar hakkinda yaklasik 10 c�mle ile kisa bir paragraf yazin.
# Se�imlerinizi �alisma s�resi ve depolama boyutu a�isindan a�iklayin. (Time & Space Complexity)


# Once talep edene once gondermek gerektigi icin Queueu ver yapisi kullanilir.
# Oncelikle ilk queue yapisinda tum talepler gelis sitasina gore enque komutuyla siraya alinir,
# atrica her bir yazici icin de queue yapisi kullaniriz
# 64 yazicimiz oldugu icin tum talepler baslangicta yazicilara esit bir sayida gonderilir mesela 5 er tane
# bir is bitiren yazici en ondeki isi dequeue komutuyla kuyruktan cikartilir.
# belli araliklarla yazicilarda hala kuyrukta sayisi tespit edilip isi dahacabuk biten yaziciya mesela 3 e dusene tekrar
# 2 tane gonderirilir ama hala 4 ve 5 olana yeni bir is gondermeyiz

