from _datetime import datetime

name = input("Enter your name:")
surname = input("Enter your surname:")
birth_date = input("Enter your date of birth (in DD-MM-YYYY format):")

try:
    datetime.strptime(birth_date, "%d-%m-%Y")
except ValueError:
    print("Invalid date format. Please enter the date in DG-MM-YYYY format.")

vowels_tr = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']
consonants_tr = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']

def calculate_number_of_letters(text):
    vowels = 0
    consonants = 0

    for letter in text:
        if letter.lower() in vowels_tr:
            vowels += 1
        elif letter.lower() in consonants_tr:
            consonants += 1

    return vowels, consonants

def birth_date_divisible_3(birth_date):
    total = 0
    for letter in birth_date:
        if letter.isdigit() and int(letter) %3 == 0:
            total += int(letter)
    return total

vowels_name, consonants_name = calculate_number_of_letters(name)
vowels_surname, consonants_surname = calculate_number_of_letters(surname)

total_number_of_vowels = vowels_name + vowels_surname
total_number_of_consonants = consonants_name + consonants_surname

total_divided_by_three = birth_date_divisible_3(birth_date)

lucky_number = "{}{}{}".format(total_number_of_vowels,
                               total_number_of_consonants,
                               total_divided_by_three)

print("Your lucky number: {}".format(lucky_number))




