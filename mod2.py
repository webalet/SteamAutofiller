from pyautogui import write, press
from CustomerForm import main_CustomerForm
import win32clipboard
from mod1 import extract_info_from_text

is_form_open = False
current_month = 0
current_year = 23

def run_program():
    global is_form_open, current_month, current_year

    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    sixteen_digit_numbers, _, three_digit_numbers, month, year = extract_info_from_text(text)

    if int(year) > 2000:
        year = int(year) - 2000 + 1

    month = int(month) + 1

    if sixteen_digit_numbers:
        write(sixteen_digit_numbers)
        press('tab')
        if not int(month) == current_month:
            if int(month) < current_month:
                for i in range(current_month - int(month)):
                    press('up')
            else:
                for i in range(int(month) - current_month):
                    press('down')
            current_month = int(month)
        
        press('tab')

        if not is_form_open:
            press('down')
            is_form_open = True

        if not int(year) == current_year:
            if int(year) < current_year:
                for i in range(current_year - int(year)):
                    press('up')
            else:
                for i in range(int(year) - current_year):
                    press('down')
            current_year = int(year)

        press('tab')
        write(three_digit_numbers)
    else:
        print("Yanlış kart bilgileri")

