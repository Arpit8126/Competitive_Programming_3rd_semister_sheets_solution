marks=[]
elements=int(input())
for i in range(elements):
    mark=int(input())
    marks.append(mark)
pass_count=0
fail_count=0
for i in marks:
    if(i>=35):
        pass_count+=1
    else:
        fail_count+=1
print(pass_count," ",fail_count)
