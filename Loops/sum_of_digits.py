num=int(input("Enter the number : "))
sum=0
while(num>0):
    digit=num%10
    num=num//10
    sum+=digit
print(sum)