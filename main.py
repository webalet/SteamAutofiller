import hashlib, os, sys, tempfile, keyboard
from mod1 import extract_info_from_text
from mod2 import run_program, is_form_open
from CustomerForm import main_CustomerForm

def sifrele(sifre):
    return hashlib.sha256(sifre.encode("utf-8")).hexdigest()

# sabit şifre
sifre_hash = sifrele("1234")

# syslog.txt dosyasını %temp% dizininde oluştur
dosya_yolu = os.path.join(tempfile.gettempdir(), "syslog.txt")

# dosya yoksa oluştur
if not os.path.exists(dosya_yolu):
    open(dosya_yolu, "w").close()

# yanlış şifre girilirse pw modülünü çağır
def yanlis_sifre():
    import pw
    pw.run_pw()
    sys.exit()

# şifre doğru ise ana döngüye devam et
with open(dosya_yolu, "r") as file:
    ana_dongu = file.read().strip() == sifre_hash
if not ana_dongu:
    while True:
        password = input("Ay Noluyo noluyoooo \n")
        if sifrele(password) == sifre_hash:
            print("Hoşgeldin Sahip \nF2---Kopyalanan CCyi yapıştır \nF3---Restart \nF4---Çıkış\n\n\n")
            with open(dosya_yolu, "w") as file:
                file.write(sifre_hash)
            ana_dongu = True
            break
        yanlis_sifre()

# ana döngü
while ana_dongu:
    if keyboard.is_pressed('f3'):
        os.system('cls' if os.name == 'nt' else 'clear')  # konsolu temizle
        os.execv(sys.executable, ['python'] + sys.argv)
    elif keyboard.is_pressed('f2'):
        run_program()
        if not is_form_open:
            main_CustomerForm()
            is_form_open = True
    elif keyboard.is_pressed('f4'):
        ana_dongu = False
        break
