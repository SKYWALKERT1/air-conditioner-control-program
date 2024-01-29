import random
import time


class Kumanda():
    def __init__(self, klima_durum="Kapalı", klima_derece=24, marka_listesi=["Samsung"], marka="Samsung",klima_modu='soguk'):
        self.klima_durum = klima_durum
        self.klima_derece = klima_derece
        self.marka_listesi = marka_listesi
        self.marka = marka
        self.klima_modu=klima_modu

    def klima_ac(self):
        if (self.klima_durum == "Açık"):
            print("Klima zaten açık")
        else:
            print("Klima açılıyor...")
            time.sleep(2)
            self.klima_durum = "Açık"

    def klima_kapat(self):
        if (self.klima_durum == "Kapalı"):
            print("Klima zaten kapalı")
        else:
            print("Klima kapanıyor...")
            self.klima_durum == "Kapalı"

    def derece_ayarları(self):
        while True:
            cevap = input("Dereceyi Azalt: '<'\nDereceyi Artır: '>'\nCıkıs : cıkıs")

            if (cevap == "<"):
                if (self.klima_derece != 18):
                    self.klima_derece -= 1
                    print("Derece:",self.klima_derece)
            elif (cevap == ">"):
                if (self.klima_derece != 31):

                    self.klima_derece += 1

                    print("Derece:",self.klima_derece)
            else:
                print("Derece Güncellendi:",self.klima_derece)
                break

    def marka_ekle(self, Marka_ismi):

        print("Marka Ekleniyor ...")
        time.sleep(1)

        self.marka_listesi.append(Marka_ismi)

        print("Marka Eklendi......")

    def rastgele_marka(self):
        rastgele = random.randint(0, len(self.marka_listesi) - 1)
        self.marka = self.marka_listesi[rastgele]
        print("Şuan ki kanal:", self.marka)
    
    def klima_modu_ayarla(self):
        mod = input("Klima modunu girin (Soğuk/Sıcak): ")
        if mod.lower() == "soğuk":
            self.klima_modu = "Soğuk"
            print("Soğuk mod ayarlandı.")
        elif mod.lower() == "sıcak":
            self.klima_modu = "Sıcak"
            print("Sıcak mod ayarlandı.")
        else:
            print("Geçersiz mod.")

    def __len__(self):
        return len(self.marka_listesi)

    def __str__(self):
        return "Klima Durumu:  {}\nDerece Ayarı: {}\nKlima Marka Listesi: {}\nŞuanki Marka: {}\nKlima Modu: {}\n".format(self.klima_durum,self.klima_derece,self.marka_listesi,self.marka,self.klima_modu)

kumanda = Kumanda()

print(""""                                                                                                      

Cok Fonksiyonlu Klima Uygulaması

1.Klimayı Aç

2.Klimayı Kapat

3.Derece  Ayarları

4. Marka Ekle

5. Marka Sayısını Öğrenme

6. Rastgele Markaya Geçme

7.İslem Yaptıgınız Bütün Bilgiler

8.Yetkili Servis Elemanlar
      
9.Klima modu

Çıkmak için 'q' ya basın.
""")
while True:
    islem = input("İşlemi Seçiniz:")

    if (islem == 'q'):
        print("Program Sonlandırılıyor...")
        break

    elif (islem == "1"):
        kumanda.klima_ac()
    elif (islem == "2"):
        kumanda.klima_kapat()

    elif (islem == '3'):
        kumanda.derece_ayarları()
    elif (islem == '4'):
        marka_isimleri = input("Marka İsimlerini ',' ile ayrırarak girin:")
        marka_listesi = marka_isimleri.split(",")
        for eklenecekler in marka_listesi:
            kumanda.marka_ekle(eklenecekler)
    elif (islem == '5'):

        print("Marka Sayısı:", len(kumanda))
    elif (islem == '6'):
         kumanda.rastgele_marka()
    elif (islem == '7'):
        print(kumanda)
    elif (islem == '8'):
        time.sleep(1)
        print("Yetkili Servise Hoşgeldiniz Sizin icin 2 elemanımız vardır.Arıza oluştuğunda onlara e_mail'dan ulaşabilirsiniz...")
        time.sleep(2)
        class Yetkili_kisi1:
         def _init_(self,adi,soyadi,e_mail):
            self.adi=adi
            self.soyadi=soyadi
            self.e_mail=e_mail

        class Yetkili_kisi2(Yetkili_kisi1):
         def _init_(self, adi, soyadi, e_mail):
             super()._init_( adi, soyadi, e_mail)
        Hasan = Yetkili_kisi1('Hasan','Yazar','Hasan_yazarr@gmail.com')
        Furkan = Yetkili_kisi2('Furkan','Kaya','Furkan_kayaa@gmail.com')
    elif (islem==8):
        
        print("Ad:",Hasan.adi,"Soyadı:",Hasan.soyadi,"e_mail:",Hasan.e_mail)
        print("Ad:",Furkan.adi,"Soyadı:",Furkan.soyadi,"e_mail:",Furkan.e_mail)
    elif (islem=='9'):
        kumanda.klima_modu_ayarla()
    else:
        print("Gecersiz islem...")