another_try = True
entry = 3
while another_try:
    print(f"You have {entry} tries left")
    password_entry = str(input("Please enter your password: \n"))
    password = "Herring917!"
    if password_entry == password:
        another_try = False
        print("Welcome")
    elif password_entry != password:
        entry -= 1
    if entry == 0:
        another_try = False
        print("Access Denied")