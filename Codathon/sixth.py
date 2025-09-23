n=int(input())
result=[]
for i in range(n):
    a=int(input())
    odd_sum=0
    even_sum=0
    while(a>0):
        r=a%10
        a=a//10
        if(r%2==0):
            even_sum+=r
        else:
            odd_sum+=r
    if(even_sum%4==0 or odd_sum%3==0):
        result.append("Yes")
    else:
        result.append("No")
for a in result:
    print(a)
