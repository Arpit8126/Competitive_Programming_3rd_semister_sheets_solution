list=[]
n=int(input("Enter the number of elements : "))
for i in range(n):
    element=int(input("Enter element : "))
    list.append(element)
increament_value=int(input("Enter the increament number : "))
print(list)
new_list=list(map(lambda x:x+increament_value,list))
print("The new list is : ",new_list)