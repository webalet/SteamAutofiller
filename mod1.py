import re


def extract_info_from_text(text):
    pattern = re.compile(r'\b\d{16}\b')
    pattern2 = re.compile(r'\b\d{2}\b')
    olasidurum = re.compile(r'\b\d{4}\b')
    pattern3 = re.compile(r'\b\d{3}\b')

    if text is not None and len(text) > 23:
        matches = pattern.search(text)

        if matches is not None:
            sixteen_digit_numbers = matches.group(0)
            substring = text[text.index(sixteen_digit_numbers):text.index(
                sixteen_digit_numbers) + 100] if len(text) >= 100 else text[text.index(sixteen_digit_numbers):len(text)]
            matches2 = pattern2.findall(substring)
            matches3 = pattern3.search(substring)
            olasitext = olasidurum.search(substring)

            if len(matches2) == 2:
                sixteen_digit_numbers = sixteen_digit_numbers[:16]
                two_digit_numbers = matches2[0] + matches2[1]
                if not two_digit_numbers.isdigit():
                    # Son iki haneli sayı iki basamaklı sayılarla eşleşmezse "Yok" olarak ayarlanır.
                    two_digit_numbers = "Yok"

            elif olasitext and len(matches2) >= 1:
                for match in matches2:
                    sixteen_digit_numbers += match + "-"
                    break
                sixteen_digit_numbers = sixteen_digit_numbers[:16]
                two_digit_numbers = olasitext.group(0)
                if not two_digit_numbers.isdigit():
                    # Son iki haneli sayı iki basamaklı sayılarla eşleşmezse "Yok" olarak ayarlanır.
                    two_digit_numbers = "Yok"

            else:
                i = 0
                for match in matches2:
                    i += 1
                    if i == 1:
                        sixteen_digit_numbers += '-'
                    sixteen_digit_numbers += match
                    if i == 2:
                        break
                sixteen_digit_numbers = sixteen_digit_numbers[:16]
                # Son iki haneli sayı yoksa "Yok" olarak ayarlanır.
                two_digit_numbers = "Yok"

            if matches3 is not None:
                three_digit_numbers = matches3.group(0)
            elif olasitext is not None:
                matches4 = re.search(
                    pattern3, substring[substring.index(olasitext.group(0)):])
                if matches4 is not None:
                    three_digit_numbers = matches4.group(0)
                else:
                    # Son üç haneli sayı yoksa "Yok" olarak ayarlanır.
                    three_digit_numbers = "Yok"

            else:
                # Son üç haneli sayı yoksa "Yok" olarak ayarlanır.
                three_digit_numbers = "Yok"

            year_matches = re.findall(r"\b\d{2}(?!\d)\b|\b\d{4}\b", substring)
            print(year_matches)
            year = "Yok"
            month = "Yok"
            for match in year_matches:
                if len(match) == 4:
                    year = match
                    break
                elif len(match) == 2 and int(match) <= 12:
                    month = str(int(match))
                    if year != "Yok" and month != "Yok":
                        break
                else:
                    year = str(int(match))
                    if year != "Yok" and month != "Yok":
                        break

            if year == "Yok" and month == "Yok":
                if len(year_matches[0]) == 4 and int(str(year_matches[0][0])+str(year_matches[0][1])) <= 12:
                    month = str(year_matches[0][0])+str(year_matches[0][1])
                    year = str(year_matches[0][2])+str(year_matches[0][3])
                    print("month", month)
                    print("year", year)

            if year != "Yok" and len(year) == 2:
                year = "20" + year

        else:
            sixteen_digit_numbers = "Yok"
            two_digit_numbers = "Yok"
            three_digit_numbers = "Yok"
            month = "Yok"
            year = "Yok"

    else:
        sixteen_digit_numbers = "Yok"
        two_digit_numbers = "Yok"
        three_digit_numbers = "Yok"
        month = "Yok"
        year = "Yok"
    if month == "Yok":
        month = 0  # Varsayılan değer
    if year == "Yok":
        year = 23  # Varsayılan değer

    return sixteen_digit_numbers, two_digit_numbers, three_digit_numbers, month, year
