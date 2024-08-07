size=input("what is your preferred pizza size(small,medium or large) : ").strip().upper()
bill=0
if(size== 'SMALL' or size == 'S'):
    bill = 100
    var="SMALL"
elif(size == 'MEDIUM' or size == 'M'):
    bill = 200
    var="MEDIUM"
elif(size == 'LARGE' or size == 'L'):
    bill = 300
    var="LARGE"
else:
    print("You entered  a wrong or invalid input")
    exit()
    
    
    
pep= input("Do you want pepperoni on your pizza (Y/n) : ").strip().upper()
if(pep == "YES" or pep == "Y") and var == "SMALL":
    bill = bill + 30
    pepa= "pepperoni"
elif(pep == "No" or pep == "N") and var == "SMALL":
    pepa= "normal"
    pass
elif((pep == "YES" or pep == "Y") and (var == "MEDIUM" or var == "LARGE")):
    bill = bill + 50
    pepa = "pepperoni"
elif((pep == "NO" or pep == "N") and (var == "MEDIUM" or var == "LARGE")):
    pepa = "normal"
    pass
else:
    print("You entered  a wrong or invalid input")
    exit()



cheese = input("Do you want cheese (Y/N) : ").strip().upper()
if(cheese == "YES" or cheese == "Y"):
    bill = bill + 20
    ch = "with cheese"
elif(cheese == "NO" or cheese == "N"):
    ch= "without cheese"
    pass

else:
    print("You entered  a wrong or invalid input")
    exit()
var=var.lower()
print(f"You have ordered a {var} {pepa} pizza {ch},Your bill is rupees {bill}, Thankyou for your time.")

    