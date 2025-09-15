L=list(input("Enter the elements of array : ").split())
start=0
end=len(L)-1
for i in range(len(L)):
    if(start<end):
        L[start],L[end]=L[end],L[start]
        start+=1
        end-=1
print(L)