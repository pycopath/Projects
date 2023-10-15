import random

all_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,
18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36] #35:1

red_and_black = [[1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36],
[2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]]

even_and_odd = [[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36],  #1:1
[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]]

low_and_high = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],  #1:1
[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]]

dozens = [[1,2,3,4,5,6,7,8,9,10,11,12],
[13,14,15,16,17,18,19,20,21,22,23,24], [25,26,27,28,29,30,31, #2:1
32,33,34,35,36]]

columns = [[1,4,7,10,13,16,19,22,25,28,31,34], [2,5,8,11,14,
17,20,23,26,29,32,35], [3,6,9,12,15,18,21,24,27,30,33,3610]]  #2:1

six_lines = [[1,2,3,4,5,6], [4,5,6,7,8,9],[7,8,9,10,11,12],
[10,11,12,13,14,15],[13,14,15,16,17,18],[16,17,18,19,20,21],  #5:1
[19,20,21,22,23,24],[22,23,24,25,26,27],[25,26,27,28,29,30],
[28,29,30,31,32,33],[31,32,33,34,35,36]]

street = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,
18],[19,20,21],[22,23,24],[25,26,27],[28,29,30],[31,32,33],[34,35,36]]  #11:1

split = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],  #17:1
[10,11],[11,12],[12,13],[13,14],[14,15],[15,16],[16,17],[17,18],
[18,19],[19,20],[20,21],[21,22],[22,23],[23,24],[24,25],[25,26],
[26,27],[27,28],[28,29],[29,30],[30,31],[31,32],[32,33],[33,34],
[34,35],[35,36]]

#win = False

choice = ""

player_bet = ""

win_multiplier = {
    "all_numbers" : 36,
    "split" : 18,
    "street" : 12,
    "six_lines" : 5,
    "columns" : 3,
    "dozens" : 3,
    #"low_and_high" : 1.5
    #"even_and_odd" : 1.5
    #"red_and_black" : 1.5
}
#bet_amt = 0

amount = ""



def get_roulette_bet(red_and_black, even_and_odd, low_and_high, dozens, columns, six_lines, street, split, single):
    while True:
        player_bet = input("what would you like to bet on?(1 for red/black, 2 for even/odd,\
3 for low/high, 4 for dozens, 5 for columns, 6 for six numbers, 7 for streets,\
8 for splits,  9 for single): ")

        if player_bet == "1":
            choice = input("would you like to bet on red or black numbers? ")
            if choice == "red":
                choice = red_and_black[0]
                print(f"You're betting on all red numbers: {choice}")
                break
            elif choice == "black":
                choice = red_and_black[1]
                print(f"You're betting on all black numbers: {choice}")
                break


        elif player_bet == "2":
            choice = input("Would you like to bet on even or odd numbers? ")
            print("your odds are 1:2 and if you win you will be paid 1.5x your entry fee")
            if choice == "even":
                choice = even_and_odd[0]
                print(f"You're betting on all even numbers: {choice}")
                break
            elif choice == "odd":
                choice = even_and_odd[1]
                print(f"You're betting on all odd numbers: {choice}")
                break


        elif player_bet == "3":
            choice = input("Would you like to bet on low or high numbers? ")
            print("your odds are 1:2 and if you win you will be paid 1.5x your entry fee")
            if choice == "low":
                choice = low_and_high[0]
                print(f"You're betting on all low numbers: {choice}")
                break
            elif choice == "odd":
                choice = low_and_high[1]
                print(f"You're betting on all high numbers: {choice}")
                break


        elif player_bet == "4":
            choice = input("Would you like to bet on the first(1), second(2), or third(3) dozen? ")
            print("your odds are 1:3 and if you win you will be paid 3x your entry fee")
            if choice == "1":
                choice = dozens[0]
                print(f"You're betting on the first dozen: {choice}")
                break
            elif choice == "2":
                choice = dozens[1]
                print(f"You're betting on the second dozen: {choice}")
                break
            elif choice == "3":
                choice = dozens[2]
                print(f"You're betting on the third dozen: {choice}")
                break

        elif player_bet == "5":
            choice = input("Would you like to bet on the first(1), second(2), or third(3) column? ")
            print("your odds are 1:3 and if you win you will be paid 3x your entry fee")
            if choice == "1":
                choice = columns[0]
                print(f"You're betting on the first column: {choice}")
                break
            elif choice == "2":
                choice = columns[1]
                print(f"You're betting on the second column: {choice}")
                break
            elif choice == "3":
                choice = columns[2]
                print(f"You're betting on the third column: {choice}")
                break

        elif player_bet == "6":
            choice = input("You may bet on the 1st - 11th set of 6. Which do you choose? ")
            print("your odds are 1:5 and if you win you will be paid 6x your entry fee")
            if choice == "1":
                choice = six_lines[0]
                print(f"You're betting on the first set: {choice}")
                break
            if choice == "2":
                choice = six_lines[1]
                print(f"You're betting on the second set: {choice}")
                break
            elif choice == "3":
                choice = six_lines[2]
                print(f"You're betting on the third set: {choice}")
                break
            elif choice == "4":
                choice = six_lines[3]
                print(f"You're betting on the fourth set: {choice}")
                break
            elif choice == "5":
                choice = six_lines[4]
                print(f"You're betting on the fifth set: {choice}")
                break
            elif choice == "6":
                choice = six_lines[5]
                print(f"You're betting on the sixth set: {choice}")
                break
            elif choice == "7":
                choice = six_lines[6]
                print(f"You're betting on the seventh set: {choice}")
                break
            elif choice == "8":
                choice = six_lines[7]
                print(f"You're betting on the eighth set: {choice}")
                break
            elif choice == "9":
                choice = six_lines[8]
                print(f"You're betting on the ninth set: {choice}")
                break
            elif choice == "10":
                choice = six_lines[9]
                print(f"You're betting on the tenth set: {choice}")
                break
            elif choice == "11":
                choice = six_lines[10]
                print(f"You're betting on the eleventh set: {choice}")
                break

        elif player_bet == "7":
            choice = input("You may bet on the 1st - 12th street(set of 3 numbers).\
 Which do you choose? ")
            print("your odds are 1:12 and if you win you will be paid 12x your entry fee")
            if choice == "1":
                choice = street[0]
                print(f"You're betting on the first set: {choice}")
                break
            if choice == "2":
                choice = street[1]
                print(f"You're betting on the second set: {choice}")
                break
            elif choice == "3":
                choice = street[2]
                print(f"You're betting on the third set: {choice}")
                break
            elif choice == "4":
                choice = street[3]
                print(f"You're betting on the fourth set: {choice}")
                break
            elif choice == "5":
                choice = street[4]
                print(f"You're betting on the fifth set: {choice}")
                break
            elif choice == "6":
                choice = street[5]
                print(f"You're betting on the sixth set: {choice}")
                break
            elif choice == "7":
                choice = street[6]
                print(f"You're betting on the seventh set: {choice}")
                break
            elif choice == "8":
                choice = street[7]
                print(f"You're betting on the eighth set: {choice}")
                break
            elif choice == "9":
                choice = street[8]
                print(f"You're betting on the ninth set: {choice}")
                break
            elif choice == "10":
                choice = street[9]
                print(f"You're betting on the tenth set: {choice}")
                break
            elif choice == "11":
                choice = street[10]
                print(f"You're betting on the eleventh set: {choice}")
                break
            elif choice == "12":
                choice = street[11]
                print(f"You're betting on the eleventh set: {choice}")
                break

        elif player_bet == "8":
            choice = input("You may bet on the 1st - 35th split(set of 2 numbers).\
 Which do you choose? ")
            print("your odds are 1:18 and if you win you will be paid 18x your entry fee")
            if choice == "1":
                choice = split[0]
                print(f"You're betting on the first set: {choice}")
                break
            if choice == "2":
                choice = split[1]
                print(f"You're betting on the second set: {choice}")
                break
            elif choice == "3":
                choice = split[2]
                print(f"You're betting on the third set: {choice}")
                break
            elif choice == "4":
                choice = split[3]
                print(f"You're betting on the fourth set: {choice}")
                break
            elif choice == "5":
                choice = split[4]
                print(f"You're betting on the fifth set: {choice}")
                break
            elif choice == "6":
                choice = split[5]
                print(f"You're betting on the sixth set: {choice}")
                break
            elif choice == "7":
                choice = split[6]
                print(f"You're betting on the seventh set: {choice}")
                break
            elif choice == "8":
                choice = split[7]
                print(f"You're betting on the eighth set: {choice}")
                break
            elif choice == "9":
                choice = split[8]
                print(f"You're betting on the ninth set: {choice}")
                break
            elif choice == "10":
                choice = split[9]
                print(f"You're betting on the tenth set: {choice}")
                break
            elif choice == "11":
                choice = split[10]
                print(f"You're betting on the eleventh set: {choice}")
                break
            elif choice == "12":
                choice = split[11]
                print(f"You're betting on the twelfth set: {choice}")
                break
            elif choice == "13":
                choice = split[12]
                print(f"You're betting on the thirteenth set: {choice}")
                break
            if choice == "14":
                choice = split[13]
                print(f"You're betting on the fourteenth set: {choice}")
                break
            elif choice == "15":
                choice = split[14]
                print(f"You're betting on the fifteenth set: {choice}")
                break
            elif choice == "16":
                choice = split[15]
                print(f"You're betting on the sixteenth set: {choice}")
                break
            elif choice == "17":
                choice = split[16]
                print(f"You're betting on the seventeenth set: {choice}")
                break
            elif choice == "18":
                choice = split[17]
                print(f"You're betting on the eighteenth set: {choice}")
                break
            elif choice == "19":
                choice = split[18]
                print(f"You're betting on the ninteenth set: {choice}")
                break
            elif choice == "20":
                choice = split[19]
                print(f"You're betting on the twentieth set: {choice}")
                break
            elif choice == "21":
                choice = split[20]
                print(f"You're betting on the twenty-first set: {choice}")
                break
            elif choice == "22":
                choice = split[21]
                print(f"You're betting on the twenty-second set: {choice}")
                break
            elif choice == "23":
                choice = split[22]
                print(f"You're betting on the twenty-third set: {choice}")
                break
            elif choice == "24":
                choice = split[23]
                print(f"You're betting on the twenty-fourth set: {choice}")
                break
            elif choice == "25":
                choice = split[24]
                print(f"You're betting on the twenty-fifth set: {choice}")
                break
            if choice == "26":
                choice = split[25]
                print(f"You're betting on the twenty-sixth set: {choice}")
                break
            elif choice == "27":
                choice = split[26]
                print(f"You're betting on the twenty-seventh set: {choice}")
                break
            elif choice == "28":
                choice = split[27]
                print(f"You're betting on the twenty-eighth set: {choice}")
                break
            elif choice == "29":
                choice = split[28]
                print(f"You're betting on the twenty-ninth set: {choice}")
                break
            elif choice == "30":
                choice = split[29]
                print(f"You're betting on the thirtieth set: {choice}")
                break
            elif choice == "31":
                choice = split[30]
                print(f"You're betting on the thirty-first set: {choice}")
                break
            elif choice == "32":
                choice = split[31]
                print(f"You're betting on the thirthy-second set: {choice}")
                break
            elif choice == "33":
                choice = split[32]
                print(f"You're betting on the thirty-third set: {choice}")
                break
            elif choice == "34":
                choice = split[33]
                print(f"You're betting on the thirty-fourth second: {choice}")
                break
            elif choice == "35":
                choice = split[34]
                print(f"You're betting on the thirty-fifth set: {choice}")
                break


        elif player_bet == "9":
    
            choice = input("You may bet on the 1st - 36th single number in the roulette.\
 Which do you choose? ")
            print("your odds are 1:36 and if you win you will be paid 36x your entry fee")
            if choice == "1":
                choice = all_numbers[0]
                print(f"You're betting on the first number: {choice}")
                break
            elif choice == "2":
                choice = all_numbers[1]
                print(f"You're betting on the second number: {choice}")
                break
            elif choice == "3":
                choice = all_numbers[2]
                print(f"You're betting on the third number: {choice}")
                break
            elif choice == "4":
                choice = all_numbers[3]
                print(f"You're betting on the fourth number: {choice}")
                break
            elif choice == "5":
                choice = all_numbers[4]
                print(f"You're betting on the fifth number: {choice}")
                break
            elif choice == "6":
                choice = all_numbers[5]
                print(f"You're betting on the sixth number: {choice}")
                break
            elif choice == "7":
                choice = all_numbers[6]
                print(f"You're betting on the seventh number: {choice}")
                break
            elif choice == "8":
                choice = all_numbers[7]
                print(f"You're betting on the eighth number: {choice}")
                break
            elif choice == "9":
                choice = all_numbers[8]
                print(f"You're betting on the ninth number: {choice}")
                break
            elif choice == "10":
                choice = all_numbers[9]
                print(f"You're betting on the tenth number: {choice}")
                break
            elif choice == "11":
                choice = all_numbers[10]
                print(f"You're betting on the eleventh number: {choice}")
                break
            elif choice == "12":
                choice = all_numbers[11]
                print(f"You're betting on the twelfth number: {choice}")
                break
            elif choice == "13":
                choice = all_numbers[12]
                print(f"You're betting on the thirteenth number: {choice}")
                break
            elif choice == "14":
                choice = all_numbers[13]
                print(f"You're betting on the fourteenth number: {choice}")
                break
            elif choice == "15":
                choice = all_numbers[14]
                print(f"You're betting on the fifteenth number: {choice}")
                break
            elif choice == "16":
                choice = all_numbers[15]
                print(f"You're betting on the sixteenth number: {choice}")
                break
            elif choice == "17":
                choice = all_numbers[16]
                print(f"You're betting on the seventeenth number: {choice}")
                break
            elif choice == "18":
                choice = all_numbers[17]
                print(f"You're betting on the eighteenth number: {choice}")
                break
            elif choice == "19":
                choice = all_numbers[18]
                print(f"You're betting on the ninteenth number: {choice}")
                break
            elif choice == "20":
                choice = all_numbers[19]
                print(f"You're betting on the twentieth number: {choice}")
                break
            elif choice == "21":
                choice = all_numbers[20]
                print(f"You're betting on the twenty-first number: {choice}")
                break
            elif choice == "22":
                choice = all_numbers[21]
                print(f"You're betting on the twenty-second number: {choice}")
                break
            elif choice == "23":
                choice = all_numbers[22]
                print(f"You're betting on the twenty-third number: {choice}")
                break
            elif choice == "24":
                choice = all_numbers[23]
                print(f"You're betting on the twenty-fourth number: {choice}")
                break
            elif choice == "25":
                choice = all_numbers[24]
                print(f"You're betting on the twenty-fifth number: {choice}")
                break
            elif choice == "26":
                choice = all_numbers[25]
                print(f"You're betting on the twenty-sixth number: {choice}")
                break
            elif choice == "27":
                choice = all_numbers[26]
                print(f"You're betting on the twenty-seventh number: {choice}")
                break
            elif choice == "28":
                choice = all_numbers[27]
                print(f"You're betting on the twenty-eighth number: {choice}")
                break
            elif choice == "29":
                choice = all_numbers[28]
                print(f"You're betting on the twenty-ninth number: {choice}")
                break
            elif choice == "30":
                choice = all_numbers[29]
                print(f"You're betting on the thirtieth number: {choice}")
                break
            elif choice == "31":
                choice = all_numbers[30]
                print(f"You're betting on the thirty-first number: {choice}")
                break
            elif choice == "32":
                choice = all_numbers[31]
                print(f"You're betting on the thirthy-second number: {choice}")
                break
            elif choice == "33":
                choice = all_numbers[32]
                print(f"You're betting on the thirty-third number: {choice}")
                break
            elif choice == "34":
                choice = all_numbers[33]
                print(f"You're betting on the thirty-fourth second: {choice}")
                break
            elif choice == "35":
                choice = all_numbers[34]
                print(f"You're betting on the thirty-fifth number: {choice}")
                break
            elif choice == "36":
                choice = all_numbers[35]
                print(f"You're betting on the thirty-sixth number: {choice}")
                break
    spin = input("Press enter to spin!")
    while True:
        if spin == "":
            break
        else:
            break
    return choice


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




def get_roulette_spin(all_numbers):
    num = random.choice(all_numbers)
    return num


def main():
    balance = deposit()

    while True:
        answer = input("Press enter to play. Press q to quit.")
        bet_amt = input("How much money would you like to enter for this bet? $")
        #if bet_amt.isdigit:
        bet_amt = int(bet_amt)
        win = False
        if bet_amt <= 0:
            print("Your bet mus be greater than 0")
        #else:
        #    print("Your bet amount must be a number.")
        #    continue
        balance -= bet_amt
        if answer == "q":
            quit()

        bet = get_roulette_bet(red_and_black, even_and_odd, low_and_high, dozens, columns, six_lines, street, split, all_numbers)
        winning_number = get_roulette_spin(all_numbers)
        while True:
            if winning_number in bet:
                win = True
                print("you win")
                if bet in red_and_black or bet in low_and_high or bet in even_and_odd:
                    bet_amt = bet_amt + bet_amt /2
                if bet in dozens or bet in columns:
                    bet_amt = bet_amt *3
                if bet in six_lines:
                    bet_amt = bet_amt *6
                if bet in street:
                    bet_amt = bet_amt *12
                if bet in split:
                    bet_amt = bet_amt *18
                if bet in all_numbers:
                    bet_amt = bet_amt *36
                break
            else:
                win = False
                print('you lose')
                bet_amt -= bet_amt
                break
        print(f"the winning number was {get_roulette_spin(all_numbers)}")
        if win is True:
            print("win is true")
            balance += bet_amt
        elif win is False:
            print("win is false")
            balance -= bet_amt
        print(f"current balance is {balance}")


main()
