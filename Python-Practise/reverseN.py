n = input("enter the string")
n.lower()
vowels = 0
for i in n:
    if i in ('a','e','i','o','u'):
        vowels += 1

print(vowels)