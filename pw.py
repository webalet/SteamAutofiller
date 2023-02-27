from colorama import Fore, Back, Style, init
import random
import os
import time

# colorama modülünü başlatın
init()
def loading_animation():
    # Yüklenme çubuğunun animasyonu
    animation = ["[{}]".format("*"* i) for i in range(1, 51)]
    for i in range(len(animation)):
        time.sleep(0.1)
        print(Fore.GREEN + Back.RED + animation[i % len(animation)], end='\r')
        print(Style.RESET_ALL, end='')


        
def hacker_art():
    # 3D ASCII sanatı
    print(Fore.RED)
    print("   _    _  _____ ______   ___   _      _____  _____  ")
    print("  | |  | ||  ___|| ___ \ / _ \ | |    |  ___||_   _| ")
    print("  | |  | || |__  | |_/ // /_\ \| |    | |__    | |   ")
    print("  | |/\| ||  __| | ___ \|  _  || |    |  __|   | |   ")
    print("  \  /\  /| |___ | |_/ /| | | || |____| |___   | |   ")
    print("   \/  \/ \____/ \____/ \_| |_/\_____/\____/   \_/   ")
    print("                                                    ")
    print("                                                   ")
    print(Style.RESET_ALL)

def get_random_files(path):
    # Rasgele dosya isimleri oluştur
    files = os.listdir(path)
    random_files = [os.path.join(path, file) for file in random.sample(files, random.randint(1, 3))]
    return random_files

def get_username():
    # Kullanıcı adı al
    return os.getlogin()

while True:
    # Önceki çıktıları temizle
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Rastgele sayı ve sembollerden oluşan bir dize oluştur
    letters = "\n abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
    result_str = ''.join(random.choice(letters) for i in range(20))
    
    # Rastgele bir bekleme süresi belirle
    wait_time = random.uniform(1, 4)
    
    # Rasgele dosya isimleri oluştur ve kullanıcı adını al
    files = get_random_files("/Users/")
    username = get_username()
    
    # Mesajları ekrana yazdır ve belirtilen süre kadar beklet
    hacker_art()
    print(Fore.GREEN + "\nŞifreler Kopyalanıyor...")
    time.sleep(wait_time)
    print(Fore.GREEN + f"\nDosyalar: {', '.join(files)}, {username}...") 
    time.sleep(wait_time)
    print(Fore.GREEN + "\nDosyalar Server.url dosyasına kopyalanıyor...")
    loading_animation()
    print(Fore.GREEN + f"\nAccess granted: MD5 {result_str}")
    time.sleep(wait_time)
