import time
print("""*************************************

THE PROGRAM FOR SAVING USER INFORMATION

TO ENTER THE PROGRAM, ENTER SOMETHING OTHER THAN 'q'.
ENTER 'q' TO EXIT.

*************************************""")
users_list = []

while True:
    choice = input("ENTER 'q' TO EXIT:")
    if choice == "q":
        break
    else:
        name = input("Enter your name:")
        surname = input("Enter your surname:")
        job = input("Enter your job:")
        birthday_year = input("Enter your birthday year:")
        age = 2024 - int(birthday_year)

        user_info = {"Name": name,
                     "Surname": surname,
                     "Job": job,
                     "Age": age}

        print("Adding a user.. Please wait!")
        time.sleep(1)
        users_list.append(user_info)
        print("User added successfully.")
        print(users_list)








    


