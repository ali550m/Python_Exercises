print("Welcome to Treasure Island game.")

first_decision = input(
    "You reached a crossroads. Which way will you go? (left or right) "
).strip().lower()

if first_decision == "left":
    print("You died!")

elif first_decision == "right":
    second_decision = input(
        "You reached a lake beside a road. Will you swim to the other side "
        "or wait for a car? (swim or car) "
    ).strip().lower()

    if second_decision == "swim":
        print("You were eaten by a shark!")

    elif second_decision == "car":
        third_decision = input(
            "A car picked you up. The driver asked you to pick a color: "
            "blue, red, or yellow? "
        ).strip().lower()

        if third_decision == "blue":
            print("He gave you money because he loves blue.")

        elif third_decision == "yellow":
            print("He threw you out of the car!")

        elif third_decision == "red":
            print("He won't speak to you until you apologize.")

        else:
            print("Invalid color. Please choose blue, red, or yellow.")

    else:
        print("Invalid choice. Please choose swim or car.")

else:
    print("Invalid direction. Please choose left or right.")