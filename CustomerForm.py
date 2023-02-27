from names import get_first_name, get_last_name
from pyautogui import write, press
import random

from faker import Faker

fake = Faker('en_US')

# Rastgele adres oluşturma
address = fake.street_address()

# Telefon numarası örnekleri
phone_numbers = []
prefix = '0532'
for i in range(5):
    suffix = ''.join(str(random.randint(0, 9)) for _ in range(8))
    phone_number = prefix + suffix
    phone_numbers.append(phone_number)

def main_CustomerForm():
    first_name = get_first_name()
    last_name = get_last_name()
    
    press('tab')
    write(first_name)
    press('tab')
    write(last_name)
    press('tab')
    write(address)
    press('tab', presses=2)
    write('Newyork')
    press('tab')
    write('C\n')
    press('tab')
    write('34000')
    press('tab', presses=2)

    phone_number = random.choice(phone_numbers)
    write(phone_number)
