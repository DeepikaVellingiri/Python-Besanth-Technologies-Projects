print("\n --------------------------------------")
print("\tCBE TOURISM TICKET BOOKING")
print("\n --------------------------------------")
print("\n")
print("\n")
print("\t welcome to CBE TOURISM ONLINE TICKET BOOKING")
print("\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("customer satisfaction is first and remaining are next to us")
print("\n")
print("\n")
print ("Available places for you are: \n 1.Maldives \n 2.Goa \n 3.Kerala \n 4.Himlayas")
places=["Maldives","Goa","Kerala","Himalayas"] 
Maldives_ticket=15000
Goa_ticket=20000
Himalayas_ticket=29999
Kerala_ticket=12555
your_package=input("Enter your package:")
if your_package in places: 
  print(f"your {your_package}​​package is booked.\n Have a great journey ") 
  no_people=int(input(f"how many tickets {your_package}​​​​​​ you want:")) 
  if your_package=="Maldives": 
   choice=no_people*Maldives_ticket 
   print(" your ticket is almost ready for ",choice,"\n wait for few seconds \n Until don't close the page")
  elif your_package=="Goa":
  	choice=no_people*Goa_ticket 
  	print(" your ticket is almost ready for ",choice,"\n wait for few seconds \n Until don't close the page")
  elif your_package=="Kerala":
  	choice=no_people*Kerala_ticket 
  	print(" your ticket is almost ready for ",choice,"\n wait for few seconds \n Until don't close the page")
  elif your_package=="Himalayas":
  	choice=no_people*Himalayas_ticket
  	print(" your ticket is almost ready for ",choice,"\n wait for few seconds \n Until don't close the page")
  else:
  	print("Currently not available")
  	print("\n")
  	print("\n")
else:
	print(" Currently not available")  
	print("\tAvailable places for you are: \n\t 1.Maldives \n\t 2.Goa \n\t 3.Kerala   \n \t4.Himlayas")
	print("\n")
	print("\n you may check our CBE TOURISM ONLINE TICKET BOOKING site properly")
	print("\t**Thankyou for choosing us**")
	print("\t Come again,Visit again")
	print("\n")	
print("##There is some additional packages for lucky customers##")
print("Can we check?.It may be you or not")
def special_offer():
      print(" ~~~~our package~~~~")
      print("1.Rs.75,000")
      print("2.Rs.95,999")
      print("3.Rs.1,55,555")
special_offer()     
def addition():
	print("1.Bus")
	print("2.Train")
	print("3.Flight")
	mode=["Bus","Train","Flight"] 
	your_mode=input ("enter mode of travel:")
	if your_mode=="Bus": 
	   print("Available")
	elif your_mode=="Train":     
	   print("Available")
    elif your_mode=="Flight": 
       print("Available")
     else:
      	print("Not available")
addition ()
print("\n")
print("\n")
print("\t Thank you")
print("visit again")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
