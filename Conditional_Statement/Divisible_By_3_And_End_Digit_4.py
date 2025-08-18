num = int(input("Enter the number: "))

if (num % 3 == 0 and num % 10 == 4):
    print("Last digit of entered number is 4 and also divisible by 3")
else:
    print("number is not meeting criteria of divisible by 3 and last digit is 4")
