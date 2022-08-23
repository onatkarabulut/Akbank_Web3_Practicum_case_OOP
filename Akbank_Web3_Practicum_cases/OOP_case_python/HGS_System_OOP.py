import datetime

class Arac:
   def __init__(
      self, 
      hgsNo, 
      isim, 
      soyisim, 
      tarih,
      saat, 
      bakiye
   ):
      self.hgsNo = hgsNo
      self.isim = isim
      self.soyisim = soyisim
      self.tarih = tarih
      self.saat = saat
      self.bakiye = bakiye
   pass
pass
      
class Otomobil(Arac):
   arac_sinif = "1.Sınıf"
   gecen_otomobiller = []
   def gecen_Otomobiller():
      if Otobus.gecen_Otobusler == []:
         print("['Bugün otomobil geçmedi.']")
      else:
         print(Otomobil.gecen_otomobiller)
pass

class Minibus(Arac):
   arac_sinif = "2.Sınıf"
   gecen_minibusler = []
   def gecen_Minibusler():
      if Minibus.gecen_minibusler == []:
         print("['Bugün minibüs geçmedi.']")
      else:
         print(Minibus.gecen_minibusler)
pass

class Otobus(Arac):
   arac_sinif = "3.Sınıf"
   gecen_otobusler = []
   def gecen_Otobusler():
      if Otobus.gecen_otobusler == []:
         print("['Bugün otobüs geçmedi.']")
      else:
         print(Otobus.gecen_otobusler)
pass

class Yonetim(): 
   
   otomobil_ucret = 50
   minibus_ucret = 100
   otobus_ucret = 150
   gunluk_odemeler = 0
   
   def elde_edilen_toplam_günlük_bakiye():
      print('Elde edilen günlük ödeme = {} '.format(int(Yonetim.gunluk_odemeler)))
   pass
pass
   
class Gise(Otomobil, Minibus, Otobus): 
   gecen_araclar = []
   def gecen_Araclar():
      print(Gise.gecen_araclar)
   pass

   def odeme(args):
      Gise.gecen_araclar.append(args.hgsNo)
      today = str(datetime.date.today())
      arg_tarih = str(args.tarih)    
      if arg_tarih == today:
         if args.arac_sinif == "1.Sınıf":
            Otomobil.gecen_otomobiller.append(args.hgsNo)
            args.bakiye -= int(Yonetim.otomobil_ucret)
            Yonetim.gunluk_odemeler += int(Yonetim.otomobil_ucret)
            print("Güncel bakiyeniz: {} TL ".format(args.bakiye))
         elif args.arac_sinif == "2.Sınıf":
            Minibus.gecen_minibusler.append(args.hgsNo)
            args.bakiye -= Yonetim.minibus_ucret
            Yonetim.gunluk_odemeler+= int(Yonetim.minibus_ucret)
            print("Güncel bakiyeniz: {} TL ".format(args.bakiye))
         elif args.arac_sinif == "3.Sınıf":
            Otobus.gecen_otobusler.append(args.hgsNo)
            args.bakiye -= Yonetim.otobus_ucret
            Yonetim.gunluk_odemeler+= int(Yonetim.otobus_ucret)
            print("Güncel bakiyeniz: {} TL ".format(args.bakiye))
         else:
            print("Kamera araç sınıfını algılayamadı.")
      else:
         print("Bugün HGS kullanan araç bulunmamakta.")
   pass
pass



if __name__ == '__main__':
   otomobil1 = Otomobil(
      'Hsg No: 123323',
      'İsim: Onat',
      'Soyisim: Karabulut',
      # '2022-08-23',
      str(datetime.date.today()),   
      '15:37',
      40
   )
   minibus1 = Minibus(
      'Hsg No: 421412',
      'İsim: Emre',
      'Soyisim: Akdemir',
      # '16-08-2022',
      str(datetime.date.today()),
      '16:02',
      1000
   )
   otobus1 = Otobus(
      'Hsg No: 627352',
      'İsim: Ali',
      'Soyisim: Güney',
      # '15-08-2022',
      str(datetime.date.today()),
      '12:34',
      750
   )
      
  
   print("""
   =============================================================
         
            ÜCRET TARİFELERİ
               1.SINIF ARACLAR: 50 TL
               2.SINIF ARACLAR: 100 TL
               3.SINIF ARACLAR: 150 TL

               uyarı: 
                  HGS hesabında geçiş için yeterli bakiye 
                  bulunmaması halinde, geçişten sonra 
                  15 (on beş) gün içerisinde yeterli 
                  tutar yatırılmadığı takdirde
                  ilgili geçişler için tebligat
                  işlemleri yapılacaktır.
               
   =============================================================                 
               
         """)
   
      #arac yollayın
   #Gise.odeme(minibus1)      
   #Gise.odeme(otobus1)
   Gise.odeme(otomobil1)
   
      #günlük bakiyeyi bastırın
   Yonetim.elde_edilen_toplam_günlük_bakiye()
   
      #gün içerisinde geçen otomobiller
   Otomobil.gecen_Otomobiller()
   
      #gün içerisinde geçen otobüsler
   Minibus.gecen_Minibusler()
   
      #gün içerisinde geçen otobüsler
   Otobus.gecen_Otobusler()
   
      #gün içerisinde gişeden geçen araçları öğrenin (dizi)
   Gise.gecen_Araclar()
pass
