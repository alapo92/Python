films = {
    # key:[min age, # of tickets]
    "Harry Potter": [15, 10],
    "Guardians": [14, 0],
    "Bourne": [18, 5],
    "Her": [12, 1],
    "Please Like Me": [14, 5],
    "The Tropical Adventures Of Penguini": [21, 100]
}

while True:
    # title to capitalise the first letter of each word
    choice = input("What film do you want to watch? :").strip().title()
    if choice in films:
        age = int(input("How old are you?: ").strip())
        # Check user age
        if age >= films[choice][0]:
            # Check number of seats

            num_seats = films[choice][1]

            if num_seats > 0:
                print("Enjoy the film!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("The tickets for this movie are sold out :(")
        else:
            print("You are too young to watch that film :(")
    else:
        print("We don't have that film...")
