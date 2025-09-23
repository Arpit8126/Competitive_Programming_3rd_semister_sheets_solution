sales=[]
elements=int(input())
max_sales = -float('inf')
min_sales = float('inf')
for i in range(elements):
    amount=int(input())
    sales.append(amount)
    if(amount>max_sales):
        max_sales=amount
    if(amount<min_sales):
        min_sales=amount
print(max_sales," ",min_sales)
