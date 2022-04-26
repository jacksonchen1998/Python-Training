from random import randint

"""

This is a game.
When user shake 7 or 11 at first time, user won.
Otherwise, user lose money.

After that, when user shake 7, user lose.
But when it shake same as first time, user won.
It will continue shake the dies, until the user has no money.

"""

money = 3000
while money > 0:
    print("You have ", money, " now")
    go_on = False
    while True:
        debt = int(input("Please input a debt: "))
        if 0 < debt <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print("The player has %d point.", first)
    if first == 7 or first == 11:
        print("Player won !!!")
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print("GM won :)")
        money -= debt
    else:
        go_on = True

    while go_on:
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print("The player has %d point.", current)
        if current == 7:
            print("GM won :)")
            money -= debt
        elif current == first:
            print("Player won !!!")
            money += debt
        else:
            go_on = True
print("Game Over")


    
