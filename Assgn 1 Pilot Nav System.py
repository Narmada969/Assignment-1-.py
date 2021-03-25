num = float(input("Enter the current altitude of the plane: "))

if (num == 3000) :
    print("ALLOWED, SAFE FOR LANDING")
elif ((num> 3000) and (num <= 6000)):
    print("ALLOWED, TRY FOR LANDING")
elif (num > 6000):
    print("GO AROUND")
