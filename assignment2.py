print("""********************************************

DICTIONARY APPLICATION

Write the Turkish translation of the words given in English.

********************************************""")

word_dict = {
    "Nursery": "Kreş",
    "Private": "Özel",
    "Chimney": "Baca",
    "Pencil": "Kalem",
    "Knee": "Diz",
    "Shoulder": "Omuz",
    "Colleague": "Meslektaş",
    "Mouse": "Fare",
    "Shirt": "Gömlek",
    "Computer": "Bilgisayar",
}

user_answers = []
correct_answers = 0
wrong_answers = 0


for word in word_dict.keys():
    answer = input("Write the Turkish translation of the '{}':".format(word))
    user_answers.append((word, answer))


for word, answer in user_answers:
    correct_answer = word_dict[word]

    if answer.lower() == correct_answer:
        print("CORRECT ANSWER! '{}'".format(correct_answer))
        correct_answers += 1
    else:
        print("WRONG ANSWER! Answer is '{}'".format(correct_answer))
        wrong_answers += 1

print("""*************************************************
RESULTS

TOTAL CORRECT ANSWERS: {}

TOTAL WRONG ANSWERS: {}
*************************************************""".format(correct_answers,wrong_answers))







