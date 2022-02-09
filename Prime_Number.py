print("Prime Number Checker")
def Prime_Number(x):
    if x%2==0:
        print("Not a prime Number!")
    elif x%3 ==0:
        print("Not a prime number")
    else:
        print("Number is Prime")

n = int(input("Enter any Number to check for Prime"))
Prime_Number(x= n)
