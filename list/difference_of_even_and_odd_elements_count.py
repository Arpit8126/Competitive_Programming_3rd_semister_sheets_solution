L=list(map(int,input("Enter the elements of array : ").split()))
even_count=0
odd_count=0
for i in L:
    if(i%2==0):
        even_count+=1
    else:
        odd_count+=1
if(even_count>odd_count):
    print(even_count-odd_count)
elif(odd_count>even_count):
    print(odd_count-even_count)