import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 5

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 12

}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2

}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("Your deposit was successful. Happy gambling!")
                break
            else:
                print("Your deposit must be greater than 0")
        else:
            print("Please enter a number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input("How many lines would you like to bet on? (1-" + str(MAX_LINES) + ") " )
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("You can only bet on 1, 2, or 3 lines.")
        else:
            print("Please enter a number.")
    return lines

def get_slot_bet():
    while True:
        amount = input("How much would you like to bet? " )
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and {MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:

        bet = get_slot_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Your bet exceeds your balance. Please play what you can afford. Your current \
balance is ${balance}")
        else:
            break


    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}.")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet

def slot_machine():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play. Press q to quit.")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

slot_machine()





#dir with all winning bets
#list with all winning bets
#define a spin
