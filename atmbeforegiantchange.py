import os,datetime
date = datetime.date.today()
# Create accounts
class Account(object):
    def __init__(self, initial):
            self.balance = initial

    def deposit(self, amt):
            self.balance = self.balance + amt
            print '\n\n\n\n\nYour balance is now $', self.balance, '\n', date
            menu()

#Withdraw money if the balance is greater than 0
    def withdraw(self,amt):
            if (self.balance - amt) > 0.0:
                    self.balance = self.balance - amt
                    print '\n\n\n\n\nYour balance is now $', self.balance, '\n', date
                    menu()
            else:
                    print 'Insufficient funds'
                    login()

#Get the account balance and print it to the screen
    def getbalance(self):
            print '\n\n\n\n\nYour balance is $', self.balance, '\n', date
            menu()
            return self.balance

#menu function ##########	Inputing strings breaks the menu ##### fix it
def menu():
    menu = '\n\n\n\n\n1) Fast Cash $40\t\t3) Withdraw\n\n2) Account Balance\t\t4) Deposit\n\n5) Exit\n'
#I'm going to try to leave sel as raw input and convert to an int on the next line
    sel = int(raw_input(menu))
#Fast cash calls the class Account and uses the withdraw function to withdraw $40 quickly.
    if sel == 1:
            os.system('clear')
            jon.withdraw(40.0)

#This will display the user's account balance
    elif sel == 2:
            os.system('clear')
            jon.getbalance()

#This will ask the user for how much they want to withdraw and convert it to a float
    elif sel == 3:
            os.system('clear')
            amt = float(raw_input("""\n\n\n\n\n
Please enter your the amount you wish to withdraw in $20 increments.\n"""))
            os.system('clear')
            ans = int(raw_input("""Are you sure you want to withdraw $ %d?\n1) Yes\n2) No\n""" % (amt)))
            if ans == 1:
                    os.system('clear')
                    jon.withdraw(amt)
            else:
                    user()

#This is for depositing
    elif sel == 4:
            os.system('clear')
            amt = float(raw_input("""\n\n\n\n\nPlease enter your the amount you wish to deposit.\n"""))
            os.system('clear')
            jon.deposit(amt)

#exit the atm
    elif sel == 5:
            os.system('clear')
            user()
    else:
            print('Wrong selection please login')
            user()

#end of menu function

jon=Account(110.00)
jon.pin = int(1234)
jon.username = 'JonS'

def user():
    username = raw_input('Enter your user name\n')
    if username == jon.username:
            login()
    else:
            print 'Wrong user name, please try again.'
            user()
#login function checks the pin and proceeds if it's correct
def login():
    pin = int(raw_input('Enter your pin\n'))
    if pin == jon.pin:
            menu()
    else:
            os.system('clear')
            print('Wrong pin, the police are on the way.')
            user()

user()


############## OUT PUT ###################
"""
Enter your user name
JonS
Enter your pin
1234





1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit



1
Your balance is now $ 70.0
2015-06-07





1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit
2




Your balance is $ 70.0
2015-06-07





1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit
3





Please enter your the amount you wish to withdraw in $20 increments.
120
Are you sure you want to withdraw $ 120?
1) Yes
2) No
Insufficient funds
Enter your pin
1234





1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit

3





Please enter your the amount you wish to withdraw in $20 increments.

20
Are you sure you want to withdraw $ 20?
1) Yes
2) No

Your balance is now $ 50.0
2015-06-07





1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit
4






Please enter your the amount you wish to deposit.
500
Your balance is now $ 550.0
2015-06-07





1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit
5
Enter your user name
JonS
Enter your Pin
1
Wrong pin, the police are on the way.
Enter your pin
1234





1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit
88
Wrong selection please login
Enter your user name

"""
