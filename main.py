# Slot Machine Game by Brianna Ysabel Cabuay

from random import randint

# allows user to deposit money
def deposit():
    try:
        bet_Amt = float(input("Hello! How much would you like to deposit? "))
        if(bet_Amt < 0):
            print("Must deposit a value greater than 0.")
            return deposit()
    except ValueError as e:
        print(f"Invalid input → {e}\n Try again.")
        return deposit()
    return round(bet_Amt, 2)
def withdraw(earnings : float, withdraw : float):
    if earnings < 0:
        print("There is nothing to withdraw!")
        return
    total = round(earnings - withdraw, 2)
    return total
def slotGame():
    winning_slots = {
        'row_0': {'col_0': "🍒", 'col_1': "🍒", 'col_2': "🍒"},
        'row_1': {'col_0': "𝟽", 'col_1': "𝟽", 'col_2': "𝟽"},
        'row_2': {'col_0': "🐲", 'col_1': "🐲", 'col_2': "🐲"}
    }
    slot_icons = ["🐲","🍒", "𝟽", "💰", "🍍"]
    game_slots = {
        'row_0': {'col_0' : "", 'col_1': "", 'col_2': ""},
        'row_1': {'col_0': "", 'col_1': "", 'col_2': ""},
        'row_2': {'col_0': "", 'col_1': "", 'col_2': ""}
    }
    for row_index in game_slots:
        for col_index in game_slots[row_index]:
            slot = randint(0, len(slot_icons) - 1)
            game_slots[row_index][col_index] = slot_icons[slot]
    for row_index in game_slots:
        row = list(game_slots[row_index].values())
        print(row)
    # return game_slots
    pass
#main
money = deposit()
print(f"You have deposited: ${deposit}")

slotGame()

withdraw_Amt = float(input(f"You have $, how much would you like to withdraw?"))
withdraw(money, withdraw_Amt)

