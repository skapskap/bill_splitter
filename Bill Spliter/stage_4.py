import random

print("How many people want to join to the party? (including you)")
number_of_people = int(input())

if number_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friend_dict = {}
    value = 0
    num_people_remaining = number_of_people
    while num_people_remaining > 0:
        name = input()
        friend_dict[name] = value
        num_people_remaining -= 1
    print("What's the final bill?")
    bill = int(input())
    print("Do you want to raffle a person to not pay the bill?")
    lucky_person = input().lower()
    if lucky_person == "yes":
        lucky = random.choice(list(friend_dict.keys()))
        print(f"{lucky} is the lucky one!")
        split_bill = round(bill / (number_of_people - 1), 2)
    else:
        lucky = None
        print("No one is going to be lucky")
        split_bill = round(bill / number_of_people, 2)

    for friend in friend_dict:
        friend_dict[friend] = split_bill
        if friend == lucky:
            friend_dict[friend] = 0

    print(friend_dict)