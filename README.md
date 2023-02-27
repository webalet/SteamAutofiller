# Steame otomatik bilgileri dolduran program.
Bu program, kullanıcıların kredi kartı bilgilerini toplamalarına yardımcı olan bir Python programıdır. Program, kullanıcının bilgisayarındaki panoyu dinler ve panoya kopyalanan herhangi bir metindeki kredi kartı bilgilerini (16 haneli kart numarası, son kullanma tarihi, güvenlik kodu vb.) otomatik olarak algılar ve bir müşteri formuna yazdırır.

## Nasıl Kullanılır
Programı çalıştırmak için, bir terminal açın ve python main.py komutunu girin. Program başlatılırken, bir şifre istenir. Varsayılan şifre "1234" olarak ayarlanmıştır. Şifreyi doğru girerseniz, ana menüye erişebilirsiniz.

Ana menüde, program klavyedeki F2, F3 ve F4 tuşlarına duyarlıdır. F2'ye basarak panoya kopyalanan kart bilgilerini ve ilk seferde kullanışta random bir şekilde isim/soyisim/telefon gibi bilgileri de otomatik olarak doldurabilirsiniz. F3'e basarak programı yeniden başlatabilirsiniz. F4'e basarak programdan çıkabilirsiniz.

## Modüller
Program, üç ayrı modül dosyası kullanır:

mod1.py: Panodan kopyalanan metindeki kredi kartı bilgilerini işleyen bir dizi yardımcı işlev içerir.
mod2.py: Müşteri formunu otomatik olarak dolduran bir işlev içerir.
pw.py: Yanlış şifre girilirse çalıştırılan bir işlev içerir. Kullanıcılara rastgele bir şifre gösterir ve bu şifreyi bir dosyaya kaydeder.
Gereksinimler
Programın doğru şekilde çalışabilmesi için, aşağıdaki Python modüllerinin kurulu olması gerekmektedir:
```bash
  hashlib
  os
  sys
  tempfile
  keyboard
  pyautogui
  win32clipboard
  names
  faker
```



### Modüllerin çoğu, birlikte yüklü Python sürümünüzde zaten yüklü olacaktır. Ancak pyautogui, win32clipboard, names ve faker modülleri yüklenmediyse, komut istemine şu komutları girerek yükleyebilirsiniz:
```bash
pip install pyautogui
pip install pywin32
pip install names
pip install faker
```



  
