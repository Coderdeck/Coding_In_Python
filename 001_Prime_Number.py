# Input : 13

# Output : Prime Number

# Input : 24

# Output : Not a Prime Number


num = int(input())

# METHOD - 01

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")


# METHOD - 02

prime = not(bool([i for i in range(2, num) if (num%i == 0)]))

print ("Prime Number" if prime else "Not a Prime Number")
