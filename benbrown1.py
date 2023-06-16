#integer birthyear

birthyear = int(input("Enter birthyear: "))

currentyear = 2023

age = currentyear - birthyear

if age >= 18:
        print("You can vote")

else:
        print("You cannot vote")

