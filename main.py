import random


# snake gun water game


# def gameWin(comp, you):
#     if comp == you:
#         return None
#     elif comp == "s":
#         if you == "w":
#             return False
#         else:
#             return True
#     elif comp == "w":
#         if you == "g":
#             return False
#         else:
#             return True
#     elif comp == "g":
#         if you == "s":
#             return False
#         else:
#             return True


# ranNo = random.randint(1, 3)
# if ranNo == 1:
#     comp = "s"
# elif ranNo == 2:
#     comp = "w"
# else:
#     comp = "g"

# print(("Comp chose snake(s) water(w) or gun(g) "))
# you = input("You tunr snake(s) water(w) or gun(g) ")

# print(f"Com chose {comp} ")
# print(f"you chose {you} ")
# a = gameWin(comp, you)
# if a == None:
#     print("The game is tie")
# elif a:
#     print("You win")
# else:
#     print("you lose")

# if comp == you:
#         return None
#     elif comp == 's':
#         if you == "w":
#             return False
#         else:
#             return True
#     elif comp == "w":
#         if you == 'g':
#             return False
#         else:
#             return True
#     elif comp == 'g':
#         if you == 's':
#             return False
#         else:
#             return True


def game(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "g":
            return True
        else:
            return False
    elif comp == "g":
        if you == "s":
            return False
        else:
            return True
    elif comp == "w":
        if you == "g":
            return True
        else:
            False


randomNo = random.randint(1, 3)
if randomNo == 1:
    comp = "s"
elif randomNo == 2:
    comp = "w"
elif randomNo == 3:
    comp = "g"

you = input("Enter Snake(s) water(w) or gun(g) ")
a = game(comp, you)

print(f"The comp chosed {comp} ")
print(f"You chosed {you} ")
if a == None:
    print("the game is tie")
elif a:
    print("You won")
else:
    print("you lose")
