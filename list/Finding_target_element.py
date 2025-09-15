list=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    element=int(input("Enter element : "))
    list.append(element)
target=int(input("Enter the target number : "))
count=0
for i in range(n):
    if(list[i]==target):
        count+=1
print(f"The number of occurance of {target} in the list is : ",count) 