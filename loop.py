sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i

print("Sum =", sum)





num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)