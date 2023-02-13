

def enter_pin(num):

    if int(num) == 3456:
        print('pin number enter suceessfully')
    else:
        print('invalid pin number')
    return enter_pin

def check_balance():
    enter_pin(input('enetr pin number: '))
    print('avaliable balance: 20000')
check_balance()

def withdraw_amount(enter_amount):
    enter_pin(input('enetr pin number: '))
    if int(enter_amount) >= 10000:
        print('suceessfully amount withdraw')
    else:
        print('insufficiant amount')
withdraw_amount(input('enter amount'))

def change_pin(new_pin,confirm_pin):
    enter_pin(input('enter old pin: '))
    if len(new_pin) == 4:
        if confirm_pin == new_pin:
            print('successfully pin number change')
        else:
            print('pin number not matched')
    else:
        print('invalid pin number')
        print('enter valid pin nuber')
new_pin = input('new pin')
confirm_pin = input('confirm pin')

change_pin(new_pin,confirm_pin)



