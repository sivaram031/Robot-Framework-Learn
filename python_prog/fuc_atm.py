
pin = 3456
avaliable_balance = 11000


flag = True
while flag:
    print("Enter 1 to Balance Enquir \n Enter 2 to withdraw money \n Enter 3 to Deposit \n Enter 4 to change pin \n Enter 5 to logut")
    num = int(input("Enter the option:"))
    if num == 1:
        print('Balance Enquary')
        if int(pin) == int(input('enter pin number')):
            print(avaliable_balance)
        else:
            print('invalid pin number')
    elif num == 2:
        if int(pin) == int(input('enter pin number')):
            withdrawal_amount = int(input('enter withdrawal amount: '))
            if avaliable_balance >= withdrawal_amount:
                print('amount withdrawed successfully')
                avaliable_balance = avaliable_balance - withdrawal_amount
            else:
                print('insufficiant amount')
        else:
            print('invalid pin')
    elif num == 3:
        deposite_amount = int(input('enter deposite amount: '))
        avaliable_balance = avaliable_balance+deposite_amount
        print(avaliable_balance)
    elif num == 4:
        new_pin = int(input('enter new pin: '))
        pin = new_pin
        print('pin number updated')
    elif num == 5:
        print('logout')
        break

