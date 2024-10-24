# Slot Machine Game by Brianna Ysabel Cabuay
from random import randint
# allows user to deposit money
def deposit():
    try:
        bet_Amt = float(input("Hello! How much would you like to deposit? "))
        if bet_Amt < 0:
            print("Must deposit a value greater than 0.")
            return deposit()
    except ValueError as e:
        print(f"Invalid input → {e}\n Try again.")
        return deposit()
    return round(bet_Amt, 2)
def bet(bet_Amt : float):
    try:
        bet = float(input("Place your bets.\n (Must be less than or equal to amt deposited.)\n"))
        if bet < 0:
            print("Must deposit a value greater than 0.")
            return bet(bet_Amt)
        if bet > bet_Amt:
            print("Must bet less than or equal to amount deposited.")
            return bet(bet_Amt)
    except ValueError as e:
        print(f"Invalid input → {e}\n Try again.")
        return bet(bet_Amt)
    print(f"You have bet: ${bet}")
    return round(bet, 2)
#allows withdrawing of earnings
def withdraw(earnings : float, withdraw : float):
    if earnings < 0:
        print("There is nothing to withdraw!")
        return
    total = round(earnings - withdraw, 2)
    return total
#slot game
def slotGame(earnings : float, bet : float):
    #all slot possibilities
    slot_icons = ["🐲","🍒", "𝟽", "💰", "🍍"]
    #placeholder for user's slots
    game_slots = {
        'row_0': {'col_0' : "", 'col_1': "", 'col_2': ""},
        'row_1': {'col_0': "", 'col_1': "", 'col_2': ""},
        'row_2': {'col_0': "", 'col_1': "", 'col_2': ""}
    }
    #assigns a random slot icon to each slot to create randomized set
    for row_index in game_slots:
        for col_index in game_slots[row_index]:
            slot = randint(0, len(slot_icons) - 1)
            game_slots[row_index][col_index] = slot_icons[slot]
    #prints randomized set
    for row_index in game_slots:
        row = list(game_slots[row_index].values())
        print(row)
    all_icons = ""
    #assigns all icons to a single string
    for row_index in game_slots:
        for icon in game_slots[row_index].values():
            all_icons = all_icons + icon
    #iterates through string to check for one of winning combinations
    middle_slot = all_icons[3: -3]
    win = True
    for letter in range(len(middle_slot)):
        if not middle_slot[0] == middle_slot[letter]:
            win = False
    #win or loss logic
    if win:
        earnings = earnings + (bet * 2)
    else:
        earnings = earnings - bet
    return earnings
def main():
    print("Welcome to Slot Machine!\n🎰🎰🎰🎰🎰" +
          "\nRules:" +
          "\n1) To play, please deposit money.(Must be greater than 0)\n" +
          "\n2) Decide how much to bet and press enter.\n"
          " (If you win, this amount is doubled, if you lose, it is subtracted.)\n"
          "\n3) Once you've either run out of money or decided to stop playing,\n"
          "your earnings will be displayed, and you will be asked to play again\n"
          "or withdraw your earnings.\n")
    money = deposit()
    print(f"You have deposited: ${money}")
    user_bet = bet(money)
    money = slotGame(money, user_bet)
    continue_play = True
    while money > 0 and continue_play:
        continue_play = input(f"You have: ${money}. Would you like to play again? (y/n) ")
        if continue_play == "y":
            user_bet = bet(money)
            money = slotGame(money, user_bet)
        else:
            continue_play = False

    print("Thank you for playing!")
    end_game = input("Would you like to deposit and play more or wihdraw your earnings? (d/w)")
    if end_game == "d":
        print("First, let's withdraw your leftover earnings")
        main()
    elif end_game == "w":
        withdraw_amt = float(input(f"You have ${money}, how much would you like to withdraw?"))
        withdraw(money, withdraw_amt)
    else:
        print("Invalid input")
        exit()
main()