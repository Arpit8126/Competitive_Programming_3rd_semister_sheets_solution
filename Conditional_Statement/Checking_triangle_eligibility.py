a=int(input("Enter first angle of triangle : "))
b=int(input("Enter second angle of triangle : "))
c=int(input("Enter third angle of triangle : "))
sum=a+b+c
if(sum==180):
    print("Given angles are forming a triangle ")
else:
    print("Given angles are not forming a triangle ")