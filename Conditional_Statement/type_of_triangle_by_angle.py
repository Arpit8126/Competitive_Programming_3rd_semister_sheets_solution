a=int(input("Enter first angle of triangle : "))
b=int(input("Enter second angle of triangle : "))
c=int(input("Enter third angle of triangle : "))
if(a==90 or b==90 or c==90):
    print("Right angle triangle ")
elif(a>90 or b>90 or c>90):
    print("Obtuse  angle triangle ")
elif(a<90 or b<90 or c<90):
    print("Acute angle triangle ")
