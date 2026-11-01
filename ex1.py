print("********** WONDER WORLD ADVENTURE PARK **********")
print("Welcome to Wonder World!")

age = int(input("Enter your age: "))

if age >= 18:
    print("Welcome! You are eligible for all rides.")

    ride = input("Enter your ride (rollercoaster, waterpark, kids): ")

    if ride == "rollercoaster":
        
        print("You selected Roller Coaster.")
        height = int(input("Enter your height in cm: "))
        if height >= 140:
            print("Enjoy your roller coaster ride!")
        else:
            print("Sorry, your height is too short.")
    elif ride == "waterpark":
        print("Welcome to the water park!")
        swimming = input("Do you know swimming (yes/no): ")
        if swimming == "yes":
            print("Enjoy your swimming!")
        else:
            print("Please wear a life jacket.")
    elif ride == "kids":
        print("You selected Kids Zone.")
        print("Enjoy your ride!")
    else:
        print("Sorry, this ride is not available.")
elif age >= 10:
    print("You are eligible for selected rides.")
    permission = input("Do you have parental permission (yes/no): ")
    if permission == "yes":
        print("Welcome to the kids adventure zone!")
    else:
        print("Sorry, parental permission is required.")

else:
    print("Sorry, you are too young to enter alone.")
