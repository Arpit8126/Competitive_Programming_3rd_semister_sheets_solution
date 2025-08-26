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

'''
1
01
101
0101
10101
'''

def pattern_6(n):
    for i in range(1,n+1):
        for j in range(i,0,-1):
            if(j%2==0):
                print(0,end="")
            else:
                print(1,end="")
        print()

'''
*   *
*   *
*   *
*   *
*   *
'''

def pattern_7(n):
    for i in range(n):
        print("*",end="")
        for j in range(n-2):
            print(" ",end="")
        print("*")

'''
*     *
*    *
*   *
*  *
* *
'''

def pattern_8(n):
    for i in range(n):
        print("*",end="")
        for j in range(n-i):
            print(" ",end="")
        print("*")

'''
    *
   **
  ***
 ****
*****
'''

def pattern_9(n):
    for i in range(n):
        for j in range(1,n-i):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        print()

'''
 ****
  ***
   **
    *
'''

def pattern_10(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end="")
        for j in range(1,n-i):
            print("*",end="")
        print()
    
'''
**********
****  ****
***    ***
**      **
*        *
'''

def pattern_11(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for j in range(0,2*i):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        print()

'''
*        *
**      **
***    ***
****  ****
'''

def pattern_12(n):
    for i in range(1,n):
        for j in range(i):
            print("*",end="")
        for j in range((2*n)-(2*i),0,-1):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()

'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
'''

def pattern_13(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        for j in range(0,2*i):
            print(" ",end="")
        for j in range(n-i):
            print("*",end="")
        print()
    for i in range(1,n):
        for j in range(i):
            print("*",end="")
        for j in range((2*n)-(2*i),0,-1):
            print(" ",end="")
        for j in range(i):
            print("*",end="")
        print()

'''
1
12
123
1234
12345
'''

def pattern_14(n):
    for i in range(n):
        for j in range(1,i+2):
            print(j,end="")
        print()

'''
12345
1234
123
12
1
'''

def pattern_15(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end="")
        print()

'''
54321
4321
321
21
1
'''

def pattern_16(n):
    for i in range(n):
        for j in range(n-i,0,-1):
            print(j,end="")
        print()

'''
    *
   ***
  *****
 *******
*********
'''

def pattern_17(n):
    for i in range(1,n+1):
        for j in range(n-i,0,-1):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
        print()



def output():
    a=int(input("Enter the no of rows : "))
    pattern_17(a)

output()
