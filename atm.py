import os
# Create accounts
class Account(object):
	def __init__(self, initial):
		self.balance = initial
	
	def deposit(self, amt):
		self.balance = self.balance + amt
	
#Withdraw money if the balance is greater than 0
	def withdraw(self,amt):
		if (self.balance - amt) > 0.0:
			self.balance = self.balance - amt
			print '\n\n\n\n\nYour balance is now $', self.balance
		else:
			print 'Insufficient funds'

#Get the account balance and print it to the screen
	def getbalance(self):
		print '\n\n\n\n\nYour balance is $', self.balance
		return self.balance
	
	def password(self):
		if password == password:
			print 'it worked'
			return True
#menu function	
def menu():
	menu = """\n\n\n\n\n
1) Fast Cash $40		3) Withdraw

2) Account Balance		4) Deposit

5) Exit
"""
	sel = int(raw_input(menu))
	return sel

jon=Account(110.00)
jon.pin = int(1234)


"""
class to do the account checking

username in db ?
	if not fail
		password = password in db?
			if not fail
		proceed
"""

# menu

#username = raw_input('Enter your user name\n')
def login():
	pin = int(raw_input('Enter your pin\n'))
	if pin == jon.pin:
		pass
	else:
		os.system('clear')
		print('Wrong pin, the police are on the way.')
		login()

#os.system('clear')
login()

while True:
	sel = menu()
#Fast cash calls the class Account and uses the withdraw function
#to withdraw $40 quickly.
	if sel == 1:
		os.system('clear')
		jon.withdraw(40.0)

#This will display the user's account balance
	elif sel == 2:
		os.system('clear')
		jon.getbalance()

#This will ask the user for how much they want to withdraw and
#convert it to a float
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
			pass

#This is for depositing
	elif sel == 4:
		pass

	elif sel == 5:
		os.system('clear')		
		login()#call the login function you about to write
