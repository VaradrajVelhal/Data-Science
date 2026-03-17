n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))

if n1 == n2 == n3:
    print("All are equal.")
elif n1 > n2 and n1 > n3:
    print(f"{n1} is greatest")
elif n2 > n1 and n2 > n3:
    print(f"{n2} is gretest.")
else:
    print(f"{n3} is greatest.")