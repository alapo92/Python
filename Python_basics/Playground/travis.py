known_users = ["Peter", "John", "Alice", "Cleo"]

# print(len(known_users))

while True:
    print("Hi! My name is Travis")
# strip to get rid of spaces, capitalize to accept non-capitalised input
    name = input("what is your name?: ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
# lower method to avoid Y
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == 'y':
            known_users.remove(name)
        elif remove == 'n':
            print("No problem, I didn't want you to leave anyway!")
    else:
        print("I don't think we've met before {}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == 'y':
            known_users.append(name)
        elif add_me == 'n':
            print("Alright mate, suit yourself")
