print("How many people want to join to the party? (including you)")
number_of_people = int(input())

if number_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friend_dict = {}
    value = 0
    while number_of_people > 0:
        name = input()
        friend_dict[name] = value
        number_of_people -= 1
    print(friend_dict)


# friends = []
#
# while number_of_people > 0:
#     name = input()
#     friend_dict = {name: 0}
#     friends.append(friend_dict)
#     number_of_people -= 1
#
# print(friends)