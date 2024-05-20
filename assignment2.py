print("""********************************************

DICTIONARY APPLICATION

Write the Turkish translation of the words given in English.

********************************************""")

word_list = ["Water","Computer","Pencil","Shirt","Mouse"]
word_list_tr = ["Su","Bilgisayar","Kalem","Gömlek","Fare"]

while True:
    first_word = input("Water: ")
    second_word = input("Computer: ")
    third_word = input("Pencil: ")
    fourth_word = input("Shirt: ")
    fifth_word = input("Mouse: ")

    if first_word.lower() == "su":
        print("1- CORRECT ANSWER!")
    else:
        print("1- WRONG ANSWER! Answer is", word_list_tr[0])

    if second_word.lower() == "bilgisayar":
        print("2- CORRECT ANSWER!")
    else:
        print("2- WRONG ANSWER! Answer is", word_list_tr[1])

    if third_word.lower() == "kalem":
        print("3- CORRECT ANSWER!")
    else:
        print("3- WRONG ANSWER! Answer is", word_list_tr[2])

    if fourth_word.lower() == "gömlek":
        print("4- CORRECT ANSWER!")
    else:
        print("4- WRONG ANSWER! Answer is", word_list_tr[3])

    if fifth_word.lower() == "fare":
        print("5- CORRECT ANSWER!")
    else:
        print("5- WRONG ANSWER! Answer is", word_list_tr[4])

    break







