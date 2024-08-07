height = int(input("what is your height in feet : "))
bill=0
if(height>3):
    age=int(input("What is your age : "))
    if(age<12):
        bill=150
    elif(age<=18):
        bill=250
    else:
        bill=500
    photo=input("Do you want to take a photo (Y/N) : ")
    if(photo == "Y" or photo == "y"):
        bill=bill+50
    elif(photo == "N" or photo == "n"):
        bill=bill
    else:
        print("Wrong or invalid input try again")
    print(f"your bill is rupees {bill}, have a wonderful time here")
    
else:
    print("You cant ride")
    
    
#The mistake i did is, if photo == "Y" or "y" , the value of y will always be true making the photo value always true
# i could have also did like  photo = input("Do you want to take a photo (Y/N): ").strip().upper()
# strip is used to strip of any spaces in the string and upper for making it caps.
#insted of using bill = bill there you can also go for pass, it will work exactly the same.