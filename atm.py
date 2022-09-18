print(" ***********************************")
print(" #   welcome to CBE ATM     #")
print(" **********************************")
users=["preethi","prabu","Priya"]
atmpins= [1111, 1234, 2222]
user = input("\nENTER USER NAME: ")
user = user.lower()
if user in users:
	if user == users[0]:
		print(" valid username")
		pin=int(input("enter your password:"))
		if pin in atmpins:
		    if pin == atmpins[0]:
		     print("successful ")
		    else:
		    	print(" pin incorrect")		
	elif user == users[1]:
		print(" valid username")
		pin=int(input("enter your password:"))
		if pin in atmpins:
		    if pin == atmpins[1]:
		     print("successful ")
		    else:
		     	print(" pin incorrect")
	elif user == users[2]:
		print(" valid username")
		pin=int(input("enter your password:"))
		if pin in atmpins:
		    if pin == atmpins[2]:
		     print("successful ")
		    else:
		     	print(" pin incorrect")
		     	print("\n")	
else:
		print(" \n")
		print("\t~~~~~~~~~~~~~~~~~~")
		print(" \t~Warning message~")
		print("\t INVALID USERNAME")
class BankAccount:
	balance=0
	def withdraw(self,amount):
		self.balance-=amount
		return self.balance
	def deposit(self,amount):
			self.balance+=amount
			return self.balance
	def balancecheck(self):
		print("\n new balance is. Rs.{}".format(self.balance))
	def bal_return(self):
		return(self. balance)
BT=BankAccount()
while True:
	print("\n 1.DEPOSIT \n 2.WITHDRAW \n 3.BALANCE \n 4.EXIT  ")
	ch=int(input (" Enter your choice:"))
	if ch==1:
		while True:
			amt=int(input("Enter amount to deposit"))
			if amt>0:
				BT.deposit(amt)
				break
			else:
				print("Enter valid amount:")
				continue
	if ch==2:
			while True:
				amt=int(input("Enter amount to withdraw: "))
				if BT.bal_return()>amt:
					BT.withdraw(amt)
					break
				else:
					BT.balancecheck()
					print (" \n Low balance ,please enter less amount...")
					continue
	if ch==3:
		BT.balancecheck()
	if ch==4:
		break
