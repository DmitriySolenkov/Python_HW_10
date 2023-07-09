class ATM():
    notes = []
    balance = 0
    count = 0

    def enter_sum(self):
        while (True):
            res = input(
                "Enter your sum (must be a multiple of 50, enter 0 to exit), $: ")
            try:
                sum = int(res)
                if (sum < 0):
                    print("Sum must be positive!")
                elif (sum % 50 != 0):
                    print("Sum must be a multiple of 50!")
                else:
                    return sum
            except ValueError:
                print("That's not a number!")

    def enter_menu(self):
        while (True):
            res = input()
            try:
                num = int(res)
                if (num <= 0 or num > 4):
                    print("Incorrect enter!")
                else:
                    return num
            except ValueError:
                print("That's not a number!")

    def comission(self, sum):
        if sum == 0:
            return 0
        comis = sum / 100 * 1.5
        if comis < 30:
            comis = 30
        elif comis > 600:
            comis = 600
        return comis

    def withdraw(self, balance):
        while (True):
            print("Attention! Comission will be 1.5%( min-30$, max-600$)!")
            sum = atm.enter_sum()
            if sum <= balance or sum == 0:
                break
            else:
                print("You don't have enough money!")
        comis = round(atm.comission(sum), 2)
        print("Your cash:", sum, "$")
        print("Your comission:", comis, "$")
        atm.notes.append(-sum)
        atm.notes.append(-comis)
        return (balance-sum-comis)


atm = ATM()
while (True):
    atm.balance = round(atm.balance, 2)
    if atm.balance > 5000000:
        tax = round((atm.balance*0.1), 2)
        print("Your wealth tax is", tax, "$")
        atm.balance = round(atm.balance-tax, 2)
    print("-------------------------------\nYour balance:", atm.balance, "$")
    print("Enter 1 to deposit money,\nEnter 2 to withdraw money,\nEnter 3 to check notes,\nEnter 4 to exit:")
    menu = atm.enter_menu()
    match menu:
        case 1:
            deposit = atm.enter_sum()
            atm.balance += deposit
            atm.notes.append(deposit)
        case 2:
            atm.balance = atm.withdraw(atm.balance)
        case 3:
            print(atm.notes)
        case 4:
            print("Application closed")
            break
    atm.count += 1
    if atm.count == 3:
        atm.count = 0
        if atm.balance > 0:
            bonus = round((atm.balance/100*3), 2)
            print("This is your third operation! You get bonus:", bonus, "$")
            atm.balance += bonus
            atm.notes.append(bonus)
