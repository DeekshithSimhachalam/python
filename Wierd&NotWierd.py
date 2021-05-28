n = input("Enter a number between 1 and 100:")
n = int(n)
if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print("Not weird")
    elif n >= 6 and n <= 20:
        print("Weird")
    elif n >= 20:
        print("Not Weird")
