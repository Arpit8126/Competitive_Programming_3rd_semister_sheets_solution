num = int(input("Enter the number: "))

if (num % 3 == 0 or num % 10 == 4):
    print("Either Last digit of entered number is 4 or number is divisible by 3")
else:
    print("number is not meeting criteria of divisible by 3 or last digit is 4")
