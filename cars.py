from secrets import choice


cars=["Ford","Mustang","Trueno panda","GT-R"]
while True:
    print("\nMain MENu")
    print("1.Append to the array")
    print("2.Remove from the array")
    print("3.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        number=int(input("How many cars:"))
        for i in range(number):
            newcar=input("Enter the new car name:")
            cars.append(newcar)
        for i in cars:
            print(i)
    elif choice==2:
        print("'__Removing__'")
        rem=input("Enter the car to be removed:")
        cars.remove(rem)
        for i in cars:
            print(i)
    elif choice==3:
        break
    else:
        print("Sorry incorrect choice!!")
