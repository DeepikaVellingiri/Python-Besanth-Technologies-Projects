print("	___________________________________")
print("         <<<CBE MULTISPECIALITY HOSPITAL>>>")
print("                 GANDHI STREET")
print("                   CBE")
print("                PH.NO:+91-9876543210 \n                      +91-9796954433")
print("	___________________________________")
print("\n")
slot=["USER","ADMIN"]
ch=input("Enter your appropriate field:")
requirement=ch.upper()
print("your requirement:",requirement)
if(requirement=="ADMIN"):
	print("ADMIN PAGE")
elif(requirement =="USER"):
	print("How can i help you?")
	print("\n")
	print("         ### APPOINTMENT ###")
	print("********************************")
	name=input("Enter patient name:")
	age=int(input("Enter age:"))
	token=int(input("Enter your token number  token:"))
	def fun(token):
	 if(token<=50 and token>=1):
	 	print("Appointment:\nDoctor Available between 10.00Am to 12.00 noon")
	 elif(token>=50 and token<=70):
	 	print("Appointment:\nDoctor available from 12.30 noon to 2.00 pm")
	 else:
	 	print("Appointment:\nDoctor Available from 3.30pm to 7.00pm")
	fun(token)
	print("\n")
	print("\n")
	print("         ### PRE-MEASURES###")
	def precheckup():
	  	print("*******************************")
	  	print(" 1.Weight \n 2.Temparature \n 3.Pressure ")
	def weight():
		 weight=input("enter the weight:")
		 print("weight is:",weight,"kg")
	weight()
	def temp():
		temp=input("enter the temparature:")
		print("Temparature is:",temp,"°")
	temp()
	def pressure():
		pressure=input("Enter pressure:")
		print("pressureis",pressure,"BP")
	pressure()
precheckup()
print("\n")
print("\n")
print("         ### CHECKUP###")
print("*******************************")
symptoms=input("enter symptoms:")
name=input("Enter your name:")
if(symptoms==("fever") or ("cold" ) or ("tierdness")  or ("lack of smell and taste")):
	print("\n")
	print("   ### COVID-CHECKUP###")
	print("*****************************")
	print("\n ~you have to check covid test")
	print("",name,"you have to pay Rs.2500 for covid test")
	covidtest=input("Enter covid-test result:")
	if(covidtest=="positive"):
		print("Dear patient ",name,"you affected by covid .\nYou have to quarentine yourself \n #wear your mask \n #keep 6 ft distance from others \n #sanitize yourself")
	else:
		print("Dear ",name,"your result is negative") 	
else:
	print("Dear",name,"you have normal symptoms \n")
	print("",name,"your consultation charge is Rs.500")
print("\n")
print("\n")
print("         ### MEDICINES###")
print("*******************************")
def med():
       print("Take doctor's prescribed medicines carefully \n If you have any side-effects,alergies or any problems ,         consult your doctor")
       print("   ~~GET WELL SOON~~")
med()
print("\n")
print("      ### COVID VACCINATION ###")
print(" *******************************")
def vaccination():	
  name=input("Enter your name:")
  age=int(input("Enter your age:"))
  if(age>=18):
  	print("Dear",name,"eligible to vaccinate")
  	print(" #Vaccination is need for this pandemic situation")
  else:
	  print("",name,"not eligible to vaccinate")
vaccination()
print("\n")
print("\n")
print("### COVID CASES SURVEY###")
print ("\n 1.COIMBATORE \n 2.ERODE \n 3.CHENNAI \n 4.MADURAI \n 5. SALEM \n 6.TIRCHY ")
def cases():
	district=input("Enter the district name:").upper()
	if district=="CBE":
		print("~~~~~COIMBATORE ~~~~~")
		print("2000 people affected in past  5 months")
		print("1045 people cured from the pandemic conditions")
		print("155 people are died")
	elif district=="ERODE":
		print("~~~~~ ERODE~~~~~")
		print("2500 people affected in past 5months ")
		print("1755 people cured from the pandemic conditions")
		print("745 people are died")
	elif district=="CHENNAI":
		print("~~~~~~ CHENNAI~~~~~")
		print("3000 people affected in past 5months ")
		print("2455 people cured from the pandemic conditions")
		print("775 people are died")
	elif district=="MADURAI":
		print("~~~~~ MADURAI~~~~~")
		print("950 people affected in past 5months ")
		print("699 people cured from the pandemic conditions")
		print("390 people are died")	
	elif district=="SALEM":
		print("~~~~~ SALEM~~~~~")
		print("1000 people affected in past 5months ")
		print("755 people cured from the pandemic conditions")
		print("345 people are died")
	elif district=="TIRCHY":
		print("~~~~~ TIRCHY~~~~~~")
		print("750 people affected in past 5months ")
		print("509 people cured from the pandemic conditions")
		print("241 people are died")
	else:
		print(" The district you entered is not available in our hospital survey")
cases()
