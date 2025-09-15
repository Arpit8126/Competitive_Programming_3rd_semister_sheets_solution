list=list(map(int,input("Enter the elements of array : ").split()))
for i in list:
    if(i%2!=0):
        print(i,end=" ")
        
    elif(i%2==0):
        print(i,end="")