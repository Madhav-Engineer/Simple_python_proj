#LOVE CAlCULATOR

name =input("what is your name ? : ").strip().upper() 
cname=input("what is the name of your crush ? : ").strip().upper()
namet=name.count("T")+name.count("R")+name.count("U")+name.count("E")+cname.count("T")+cname.count("R")+cname.count("U")+cname.count("E")
print(namet)
namel=name.count("L")+name.count("0")+name.count("V")+name.count("E")+cname.count("L")+cname.count("O")+cname.count("V")+cname.count("E")
print(namel)
print(f"you and your partner have a {namet}{namel} % love connection")


#Random Name Picker

#a

import random
name=input("enter the name of all your friends ,(seperated by a comma) : ").split(",")
x=random.choice(name)
print(f"{x} will pay the bill")

#b

import random
name=input("enter the name of all your friends ,(seperated by a comma) : ").split(",")
index = len(name)-1
x=random.randint(0,index)
print(f"{name[x]} will pay the bill")


#Money Hide


row1=["0","0","0"]
row2=["0","0","0"]
row3=["0","0","0"]
matrix=[row1,row2,row3]
print("This is all of your possible hide spots")
print(f"{row1}\n{row2}\n{row3}")
input=input("enter the row and colomn where you want to hide the money (seperated by comma) : ").split(",")
a=int(input[0])-1
b=int(input[1])-1
print(matrix[a][b])
matrix[a][b]="X"
print(f"{row1}\n{row2}\n{row3}")


#for loop basic

list=[1,2,3,4,5]
squares=[]
for i in list:
    square = i**2
    squares.append(square)
print(f"The squares of the given list is {squares}")

#for else loop basic

tuple=(1,2,3,4,5,6)
for i in tuple:
    if i % 8 ==0:
        print(i)
        break
else:
    print("no number in the list is divisible by 8")

#average height  without the length function or sum of list

#a
    
height=input("enter all the heights you want to take the average of (seperated by a comma) : ").split(",")
sum=0
count=0
for i in height:
    count =count+1
    sum=sum+int(i)
a=round(sum/count)
print(a)

#b

height=input("enter all the heights you want to take the average of (seperated by a comma) : ").split(",")
count=0
sum=0
for i in height:
    count+=1
for i in range(count):
    height[i]=int(height[i])
    sum = sum+height[i]
hei=round(sum/count)
print(hei)

#finding the maximum number

#a

num=input("Enter all the numbers of which you want to find the maximum of (seperated by comma): ").split(",")
count=0
for i in num:
    count+=1
    
for i in range(count):
    num[i]=int(num[i])

max=num[0]
for i in num:
    if i>max:
        max=i
print(i)

#b

num=input("Enter all the numbers of which you want to find the maximum of (seperated by comma): ").split(",")
count=0
for i in num:
    count+=1
max=int(num[0])    
for i in range(count):
    num[i]=int(num[i])
    if num[i]>max:
        max=num[i]
    
print(num[i])

#sum of all numbers between a range

#a

num=[]
for i in range(1,101):
    if i %2 ==0:
        num.append(i)
        
print(sum(num))

#b

sum=0
for i in range(2,101,2):
    sum=sum+i
print(sum)



#fizzbuzz problem

#a

for i in range(1,16):
    if i%3==0:
        if i %5==0:
            print("Fizzbuzz")
        else:
            print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)

#b
        
for i in range(1,16):
    if i%3==0 and i %5==0 :
        print("Fizzbuzz")
    elif i % 3 ==0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)
        
    
    


