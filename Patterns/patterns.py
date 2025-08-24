'''
*****
'''

def pattern_1(n):
    for i in range(n):
        print("*",end="")

'''
*****
*****
*****
*****
*****
'''

def pattern_2(n):
   for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

'''
*
**
***
****
*****
'''

def pattern_3(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end="")
        print()

'''
*****
****
***
**
*
'''

def pattern_4(n):
    for i in range(n):
        for j in range(n,i,-1):
             print("*",end="")
        print()

'''
1
1*
1*3
1*3*
1*3*5
'''

def pattern_5(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j%2==0:
             print("*",end="")
            else:
             print(j,end="")
        print()



def output():
    a=int(input("Enter the no of rows : "))
    pattern_5(a)

output()
