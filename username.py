def hint_username(username):
    if len(username) < 3:
        print("username is invalid, minimum 3 character")
    elif len(username) > 7:
        print("username is invalid , maximum character is 7")
    else:
        print("username is valid, have a nice day")

hint_username(input("Enter the username : "))