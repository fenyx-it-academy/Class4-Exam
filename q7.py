# "Yazici Ciftligi" adini verdiginiz milyon dolarlik bir is fikrine sahipsiniz.
# Pek çok insanin ofislerinde ve evlerinde yazici kullandigini biliyorsunuz ve bunun hiç mantikli olmadigini dusunuyorsunuz.
# Neden tüm yazicilari yazici çiftliginizde birlestirip, kullanicilarin yazicilarinizi kullanarak dosyalar yazdirmasini saglayip,
# bu dosyalari postayla onlara göndermeyesiniz ki?
# Elbette bu harika bir fikir, bu yüzden hemen baslamaya karar veriyorsunuz.
# Ana sorun, sunucuza gelen binlerce yazdirma komutunu islemek ve bunlari sahip oldugunuz 64 yaziciya tek tek göndermek.
# Amaç, herhangi bir baski talebini aldiktan sonra 1 saat içinde baskiyi tamamlamak ve göndermek.
# Hizmetinizin kullanici sayisinin hizla artacagini tahmin ediyorsunuz, bu nedenle isiniz büyüdükçe taleple basa çikmak için
# yeni sunucular ve yazicilar ekleyebilmeniz gerek.
# Kullanmaniz gereken veri yapilari, bu veri yapilarinin nasil uygulamaya dokulecegi ve baski hizmetini
# etkin bir sekilde çalistirmak için gerekli olacak algoritmalar hakkinda yaklasik 10 cümle ile kisa bir paragraf yazin.
# Seçimlerinizi çalisma süresi ve depolama boyutu açisindan açiklayin. (Time & Space Complexity)


# Once talep edene once gondermek gerektigi icin Queueu ver yapisi kullanilir.
# Oncelikle ilk queue yapisinda tum talepler gelis sitasina gore enque komutuyla siraya alinir,
# atrica her bir yazici icin de queue yapisi kullaniriz
# 64 yazicimiz oldugu icin tum talepler baslangicta yazicilara esit bir sayida gonderilir mesela 5 er tane
# bir is bitiren yazici en ondeki isi dequeue komutuyla kuyruktan cikartilir.
# belli araliklarla yazicilarda hala kuyrukta sayisi tespit edilip isi dahacabuk biten yaziciya mesela 3 e dusene tekrar
# 2 tane gonderirilir ama hala 4 ve 5 olana yeni bir is gondermeyiz

