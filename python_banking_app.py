'''
Managing finances can be hard for students as some lack access to wifi, data or even a mobile device. The goal of this program is to
allow students to keep track of their savings, checking accounts, withdrawals, deposits, transfers and other transactions without
the use of the internet or an online banking system. This will also allow students to add any
transaction to be recorded, hidden from any bank or institution online. If a student has not opened the program before, there will
be an option for a student to “create a new account” which creates a new output file that will begin to record savings and checking
accounts with all activity that happens concerning those accounts. If a student opens the program and already has an account, it
will ask for the name of the person and will search for the file that was saved previously to input all the financial documentation.
After that, the student will have access to five options. The student can withdraw an amount, which will subtract an amount from an 
account. The student can deposit, which will add an amount to the account and also has the option to deposit a certain percentage of
the amount in the savings account. The student will also be able to record a transaction or transfer and will specify the type
(online, debit, cash, transfer). The student will also be able to read all of their banking information and recordings within the
program. Finally, the student will be able to save all of their information and exit the program without losing it as the output
file will be updated in the Spyder folder.
'''


def new(): # creates new account file
    global first_name
    global last_name
    global date
    global chequing_balance
    global savings_balance

    with open('python_banking_app_output.txt', 'w') as fh:
        fh.write('''BANKING INFORMATION
===============================================================================
Date: ''' + date[0] + ' ' + date[1] + ', ' + date[2] + '''
Account Name: ''' + last_name + ', ' + first_name + '''

CHEQUING BALANCE: $''' + str(chequing_balance) + '''
SAVINGS BALANCE: $''' + str(savings_balance) + '''
===============================================================================
TRANSACTION HISTORY:''')


def read(): # reads all info up to date (chequing balance, savings balance, list of all previous transactions)
    info = None
    sub_list = None
    global first_name
    global last_name
    global chequing_balance
    global savings_balance
    global transactions_list
    
    # reads and prepared info from old file and prepares it into variables for new file
    with open('python_banking_app_output.txt', 'r') as fh:
        info = fh.readlines()
    sub_list = info[5].split(' ')
    chequing_balance = float(sub_list[2][1:sub_list[2].index('\n')])
    sub_list = info[6].split(' ')
    savings_balance = float(sub_list[2][1:sub_list[2].index('\n')])
    if len(info) > 9:
        transactions_list = [info[i] for i in range(9,len(info))] # list comprehension used to define list of all previous transactions
    
         
def withdraw(): # subtracts amount from account balance
    global decision
    global arbitrary_amount
    global chequing_balance
    global savings_balance
    global transactions_list
    
    # user decides which account to withdraw from
    while True:
        decision = int(input('\nWhich account would you like to withdraw from?\n1 - Chequing\n2 - Savings\n'))
        if decision != 1 and decision != 2:
            print('Invalid entry. Try again.\n')
        else:
            break
    # user decides amount
    while True:
        arbitrary_amount = float(input('\nHow much would you like to withdraw (enter only number)?: '))
        if arbitrary_amount < 0:
            print('Invalid entry. Try again.\n')
        elif decision == 1 and arbitrary_amount > chequing_balance:
            print('Invalid entry. Insufficient funds. Try again.\n')
        elif decision == 2 and arbitrary_amount > savings_balance:
            print('Invalid entry. Insufficient funds. Try again.\n')
        elif decision == 1:
            chequing_balance -= arbitrary_amount
            transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - Withdrawal from chequing account: $' + str(arbitrary_amount)))
            break
        else:
            savings_balance -= arbitrary_amount
            transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - Withdrawal from savings account: $' + str(arbitrary_amount)))
            break
    print('Transaction complete!\n')
    

def deposit(): # adds amount into account balance
    global decision
    global arbitrary_amount
    global chequing_balance
    global savings_balance
    global transactions_list
    
    # user decides what account to deposit to
    while True:
        decision = int(input('\nWhich account would you like to deposit to?\n1 - Chequing\n2 - Savings\n'))
        if decision != 1 and decision != 2:
            print('Invalid entry. Try again.\n')
        else:
            break
    # user decides how much to deposit
    while True:
        arbitrary_amount = float(input('\nHow much would you like to deposit (enter only number)?: '))
        if arbitrary_amount < 0:
            print('Invalid entry. Try again.\n')
        elif decision == 1:
            chequing_balance += arbitrary_amount
            transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - Deposit to chequing account: $' + str(arbitrary_amount)))
            break
        else:
            savings_balance += arbitrary_amount
            transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - Deposit to savings account: $' + str(arbitrary_amount)))
            break
    print('Transaction complete!\n')
    

def record(): # writes transaction/transfer with basic info
    global decision
    global arbitrary_amount
    global chequing_balance
    global savings_balance
    global recipient
    global transaction_type
    global transactions_list
    
    # user decides the type of miscellaneous transaction
    while True:
        decision = int(input('\nIs this a transfer or another type of transaction?\n1 - Transfer\n2 - Cash (undocumented)\n3 - Purchase/other\n'))
        if decision == 1:
            recipient = input('\nEnter full name of the recipient: ')
            while True:
                decision = int(input('\nWhich account would you like to withdraw from?\n1 - Chequing\n2 - Savings\n'))
                if decision != 1 and decision != 2:
                    print('Invalid entry. Try again.\n')
                else:
                    break
            # user decides amount for transfer
            while True:
                arbitrary_amount = float(input('\nHow much would you like to transfer (enter only number)?: '))
                if arbitrary_amount < 0:
                    print('Invalid entry. Try again.\n')
                elif decision == 1 and arbitrary_amount > chequing_balance:
                    print('Invalid entry. Insufficient funds. Try again.\n')
                elif decision == 2 and arbitrary_amount > savings_balance:
                    print('Invalid entry. Insufficient funds. Try again.\n')
                elif decision == 1:
                    chequing_balance -= arbitrary_amount
                    transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - Transfer to ' + recipient + ' from chequing account: $' + str(arbitrary_amount)))
                    break
                else:
                    savings_balance -= arbitrary_amount
                    transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - Transfer to ' + recipient + ' from savings account: $' + str(arbitrary_amount)))
                    break
            break
        # user inputs information on random transaction
        elif decision == 2:
            transaction_type = input("\nEnter whatever information you'd like to enter (don't forget to include the amount!): ")
            transactions_list.append('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - ' + transaction_type)
            break
        elif decision == 3:
            transaction_type = input("\nEnter the items or other information you'd like to include (not including amount): ")
            while True:
                decision = int(input('\nWhich account would you like to withdraw from?\n1 - Chequing\n2 - Savings\n'))
                if decision != 1 and decision != 2:
                    print('Invalid entry. Try again.\n')
                else:
                    break
            # user decides amount for transfer
            while True:
                arbitrary_amount = float(input('\nHow much would you like to take from the account (enter only number)?: '))
                if arbitrary_amount < 0:
                    print('Invalid entry. Try again.\n')
                elif decision == 1 and arbitrary_amount > chequing_balance:
                    print('Invalid entry. Insufficient funds. Try again.\n')
                elif decision == 2 and arbitrary_amount > savings_balance:
                    print('Invalid entry. Insufficient funds. Try again.\n')
                elif decision == 1:
                    chequing_balance -= arbitrary_amount
                    transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - ' + transaction_type + '. $' + str(arbitrary_amount) + " taken from chequing account"))
                    break
                else:
                    savings_balance -= arbitrary_amount
                    transactions_list.append(('\n\n(' + date[0] + ' ' + date[1] + ', ' + date[2] + ') - ' + transaction_type + '. $' + str(arbitrary_amount) + " taken from savings account"))
                    break
            break
        else:
            print('Invalid entry. Try again.\n')
    print('Transaction complete!\n')


def view(): # prints out transaction/transfer history
    global transactions_list

    for i in transactions_list:
        print(i)
     
    print('\n\n')


def save(): # outputs final file with updated values and transactions
    global first_name
    global last_name
    global transactions_list
    global date
    global chequing_balance
    global savings_balance

    # uses variables stored throughout program execution and outputs an updated version of original file
    with open('python_banking_app_output.txt', 'w') as fh:
        fh.write('''BANKING INFORMATION
===============================================================================
Date: ''' + date[0] + ' ' + date[1] + ', ' + date[2] + '''
Account Name: ''' + last_name + ', ' + first_name + '''

CHEQUING BALANCE: $''' + str(chequing_balance) + '''
SAVINGS BALANCE: $''' + str(savings_balance) + '''
===============================================================================
TRANSACTION HISTORY:''')
    with open('python_banking_app_output.txt', 'a') as fh:
        for i in transactions_list:
            fh.write(i)
            
    
# varaible delcaration that execute certain parts of program depending on user's interest
exit_program = None 
decision = None
first_name = ''
last_name = ''
new_account = None
chequing_balance = 0.0
savings_balance = 0.0
arbitrary_amount = 0
date = None
transactions_list = []
recipient = ''
transaction_type = None


# 'start of program' menu and asks if user wants to continue the program or exit
while True: # while loop integrated to continuously ask for inputs until input is valid
    exit_program = input('Would you like to start program (enter "yes" or "no"): ') # receive input from user
    if exit_program == 'no':
        print('Exiting program...')
        break
    elif exit_program == 'yes':
        break
    else:
        print('Invalid entry. Try again.\n')
# asks user if they already have an account - creates new file (account) or reads in file by asking their name
if exit_program == 'yes':
    while True:
        new_account = input('\nDo you already have an account? (Enter "yes" or "no"): ')
        if new_account == "yes" or  new_account == "no":
            break
        else:
            print('Invalid entry. Try again.\n')
    first_name = input('\nEnter your first name: ')
    last_name = input('\nEnter your last name: ')
    date = input('\nEnter the date (format: MONTH DAY YEAR): ')
    date = date.split(' ')
    date = (date[0], str(date[1]), str(date[2])) # date stored as tuple variable
    if new_account == "no":
        new()
    read()
# account menu where user can decide what operation they would like to perform
if exit_program == 'yes':
    while decision != 0:
        decision = int(input('''
MENU
-------------------------------------------------------------------------------
Chequeing balance = ''' + str(chequing_balance) + '''
Savings balance = ''' + str(savings_balance) + '''

OPTIONS (Enter respective number):
    
1 - WITHDRAW
2 - DEPOSIT
3 - RECORD CASH/RANDOM TRANSACTION OR BANK TRANSFER
4 - VIEW BANKING HISTORY
0 - SAVE AND EXIT PROGRAM
'''))
        if decision < 0 or decision > 4:
            print('Invalid entry. Try again.\n')
        elif decision == 1: # user wants to withdraw
            withdraw()
        elif decision == 2: # user wants to deposit
            deposit()
        elif decision == 3: # user wants to add random transaction
            record()
        elif decision == 4: # user wants to view transaction history
            view()
        else: # user wants to save data and exit
            save()
            print('Exiting program...')