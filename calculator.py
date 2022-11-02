a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
print("The first value=",a)
print("The second value=",b)
while True: 
    print("MENU")
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Exit")
    choice=int(input("Enter a choice:"))
    if choice==1:
        s=a+b
        print("Sum is",s)
    elif choice==2:
        s=b-a
        print("Subtraction of",b,"-",a,"=",s)
    elif choice==3:
        s=a*b
        print("Multiplied answer is",s)
    elif choice==4:
        s=b/a
        print("Division is",s)
    elif choice==5:
        break
    else:
        print("Sorry wrong choice!!!")
        