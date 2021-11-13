number = int(input())
order = len(str(number))
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if number == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
