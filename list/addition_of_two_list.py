L1=list(map(int,input("Enter the elements of array : ").split()))
L2=list(map(int,input("Enter the elements of array : ").split()))
new_list=[]
for i in range(len(L1)):
    new_list.append(L1[i]+L2[i])
print(new_list)