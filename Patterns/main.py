# Solid Square Star Pattern
def pattern1(n):
    print("\nPattern 1\n")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print("* ", end="")
        print()

pattern1(5)


# Left Half Pyramid Star Pattern
def pattern2(n):
    print("\nPattern 2\n")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print()

pattern2(5)


# Inverted Left Half Pyramid Star Pattern
def pattern3(n):
    print("\nPattern 3\n")
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("* ",end="")
        print()    

pattern3(5)


# Number Increasing Triangle Pattern
def pattern4(n):
    print("\nPattern 4\n")
    for i in range(1,n+1,1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()    

pattern4(5)


# Diamond Style Half Pyramid Pattern
def pattern5(n):
    print("\nPattern 5\n")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("* ",end="")
        print()    
    for i in range(n-1,0,-1):        
        for j in range(1,i+1):
            print("* ",end="")
        print()

pattern5(5)


# Right Aligned Half Pyramid Pattern
def pattern6(n):
    print("\nPattern 6\n")
    for i in range(1,n+1,1):
        for j in range(n-i,0,-1):
            print("  ",end="")
        for j in range(1,i+1):
            print('* ',end="")
        print()                    

pattern6(5)


# Inverted Right Aligned Half Pyramid Pattern
def pattern7(n):
    print("\nPattern 7\n")
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print("  ",end="")
        for j in range(1,i+1):
            print("* ",end="")   
        print()        

pattern7(5)


# Full Pyramid Star Pattern
def pattern8(n):
    print("\nPattern 8\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="") 
        print()                   

pattern8(5)


# Inverted Full Pyramid Pattern
def pattern9(n):
    print("\nPattern 9\n")
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,2*i):
            print("*",end="")
        print()    

pattern9(5)


# Right Aligned Increasing Star Triangle
def pattern10(n):
    print("\nPattern 10\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end='')
        for j in range(1,i+1):
            print("* ",end='')
        print()        

pattern10(5)


# Pattern 11 : Right Aligned Decreasing Star Triangle
def pattern11(n):
    print("\nPattern 11\n")
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print("* ",end="") 
        print()       

pattern11(5)


# Pattern 12 : Hourglass Star Pattern
def pattern12(n):
    print("\nPattern 12\n")
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ', end="")
        for j in range(1,i+1):
            print("* ",end="")
        print()     
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ', end="")
        for j in range(1,i+1):
            print("* ",end="")
        print()         

pattern12(5)


# Pattern 13 : Hollow Full Pyramid Pattern
def pattern13(n):
    print("\nPattern 13\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")     
        for j in range(1,2*i):   
            if j == 1 or j == 2*i-1 or i == n:
                print("*",end="")
            else:
                print(" ",end="")              
        print()

pattern13(5)


# Pattern 14 : Hollow Inverted Pyramid Pattern
def pattern14(n):
    print("\nPattern 14\n")
    for i in range(n,0,-1):
        for j in range(n-i):
            print(' ',end="")
        for j in range(1,2*i):
            if j == 1 or j == 2 * i-1 or i == n:
                print("*",end="")
            else:
                print(" ",end="")
        print()                

pattern14(5)


# Pattern 15 : Hollow Diamond Pattern
def pattern15(n):
    print("\nPattern 15\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,2*i):
            if j == 1 or j == 2*i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()     
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,2*i):
            if j == 1 or j == 2*i-1:
                print("*",end="")
            else:
                print(" ",end="")
        print()   

pattern15(5)


# Pattern 16 : Pascal Triangle Pattern
def pattern16(n):
    print("\nPattern 16\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print("  ", end="")
        var = 1
        for j in range(1,i+1):
            print(var,end="   ")
            var = var * (i-j) // j
        print()    

pattern16(5)


# Pattern 17 : Palindrome Diamond Number Pattern
def pattern17(n):
    print("\nPattern 17\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print("  ",end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        for j in range(2,i+1):
            print(j,end=" ")
        print()            
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print("  ",end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        for j in range(2,i+1):
            print(j,end=" ")
        print()

pattern17(4)


# Pattern 18 : Butterfly Pattern
def pattern18(n):
    print("\nPattern 18\n")
    for i in range(0,n):
        for j in range(n-i,0,-1):
            print("*",end="")
        for j in range(1,i+1):
            print(" ",end="")
        for j in range(1,i+1):
            print(" ",end="")    
        for j in range(n-i,0,-1):
            print("*",end="")    
        print()    
    for i in range(n-1,0,-1):     
        for j in range(n-i+1,0,-1):
            print("*",end="")
        for j in range(1,i):
            print(" ",end="")
        for j in range(1,i):
            print(" ",end="")
        for j in range(n-i+1,0,-1):
            print("*",end="")        
        print()                 

pattern18(5)


# Pattern 19 : Reverse Butterfly Pattern
def pattern19(n):
    print("\nPattern 19\n")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        for j in range(n-i):
            print(" ",end="")
        for j in range(n-i):
            print(" ",end="")    
        for j in range(1,i+1):
            print("*",end="")    
        print()   
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        for j in range(n-i):
            print(" ",end="")
        for j in range(n-i):
            print(" ",end="")    
        for j in range(1,i+1):
            print("*",end="")    
        print()                               

pattern19(5)


# Pattern 20 : Hollow Square Pattern
def pattern20(n):
    print("\nPattern 20\n")
    for i in range(1,n+1):
        for j in range(1,n):
            if i == 1 or i == n:
                print("*",end="")
            else:
                if j == 1 or j == n-1:
                    print("*",end="")
                else:
                    print(" ",end="")    
        print()        

pattern20(5)


# Pattern 21 : Floyd's Triangle Pattern
def pattern21(n):
    print("\nPattern 21\n")
    count = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(count,end=" ")
            count += 1
        print()    

pattern21(5)


# Pattern 22 : Binary Triangle Pattern
def pattern22(n):
    print("\nPattern 22\n")
    for i in range(1,n+1):
        for j in range(1,i+1):
            if (i+j) % 2 == 0:
                print("1",end=" ")
            else:
                print("0",end=" ")
        print()            

pattern22(5)


# Pattern 23 : Hollow Double Pyramid Pattern
def pattern23(n):
    print("\nPattern 23\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,i+1):
            if j == 1 or j == i:
                print('* ',end="")
            else:
                print("  ",end="")    
        for j in range(n-i-1):
            print("  ",end="")
        for j in range(1,i+1):
            if j == 1 and i == n:
                continue
            if j == 1 or j == i:
                print("* ",end="")   
            else:
                print("  ",end="")         
        print()        

pattern23(3)


# Pattern 24 : Hollow Butterfly Pattern
def pattern24(n):
    print("\nPattern 24\n")
    for i in range(1,n+1):
        for j in range(1,i+1):
            if j == 1 or j == i:
                print("*",end="")
            else:
                print(" ",end="")
        for j in range(1,2*n-2*i+1):
            print(" ",end="")
        for j in range(1,i+1):
            if j == 1 or j == i:
                print("*",end="")
            else:
                print(" ",end="")                
        print()
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            if j == 1 or j == i:
                print("*",end="")
            else:
                print(" ",end="")
        for j in range(1,2*n-2*i+1):
            print(" ",end="")
        for j in range(1,i+1):
            if j == 1 or j == i:
                print("*",end="")
            else:
                print(" ",end="")                
        print()            

pattern24(5)


# Pattern 25 : Hollow Pyramid Box Pattern
def pattern25(n):
    print("\nPattern 25\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,n+1):
            if j == 1 or j == n:
                print("*",end="")
            else:
                if i == 1 or i == n:
                    print("*",end="")  
                else:     
                    print(" ",end="")
        print()                

pattern25(5)


# Pattern 26 : Repeated Number Inverted Triangle Pattern
def pattern26(n):
    print("\nPattern 26\n")
    num = 1
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(num,end=" ")
        num += 1
        print()    

pattern26(6)


# Pattern 27 : Symmetric Number Pyramid Pattern
def pattern27(n):
    print("\nPattern 27\n")
    left = 1
    right = n * (n+1) + 1
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i):
            print(left,end=" ")    
            left += 1
        temp = right - i 
        for j in range(i):
            print(temp,end=" ")
            temp += 1   
        right = temp - i
        print()    

pattern27(4)


# Pattern 28 : Full Diamond Star Pattern
def pattern28(n):
    print("\nPattern 28\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print("* ",end="")    
        print()   
    for i in range(n-1,0,-1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(1,i+1):
            print("* ",end="")    
        print()          

pattern28(5)


# Pattern 29 : Diamond Palindrome Number Pattern
def pattern29(n):
    print("\nPattern 29\n")
    for i in range(1,n+1):
        for j in range(n-i):
            print("  ",end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        for j in range(2,i+1):
            print(j,end=" ")
        print()    
    for i in range(n-1,0,-1):   
        for j in range(n-i):
            print("  ",end="")
        for j in range(i,0,-1):
            print(j,end=" ")
        for j in range(2,i+1):
            print(j,end=" ")   
        print()          

pattern29(5)


# Pattern 30 : Concentric Square Number Pattern
def pattern30(n):
    print("\nPattern 30\n")
    org = n
    n = 2*n-2
    for i in range(0,n+1):
        for j in range(0,n+1):
            value = org - min(i,j,n-i,n-j)
            print(value,end=" ")
        print()    

pattern30(4)


# Pattern 31 : Alphabet Triangle Pattern
def pattern31(n):
    print("\nPattern 31\n")
    for i in range(1,n+1):
        val = n - i
        for j in range(val,n):
            print(chr(65+j),end=" ")  
        print()    

pattern31(5)


# Pattern 32 : Alternating Upper Lower Alphabet Pattern
def pattern32(n):
    print("\nPattern 32\n")
    count = 1
    for i in range(1,n+1):
        for j in range(1,i+1):
            if count % 2 == 0:
                print(chr(64+count),end=' ')
            else:
                print(chr(96+count),end=' ')
            count += 1
        print()    

pattern32(5)


# Pattern 33 : Reverse Alphabet Triangle Pattern
def pattern33(n):
    print("\nPattern 33\n")
    c1 = n
    c2 = 1
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(chr(64+c1),end=" ")
            c1 -= 1
        c1 = n - c2
        c2 += 1
        print()    

pattern33(5)


# Pattern 34 : Reverse Alphabet Triangle Pattern (Duplicate)
def pattern34(n):
    print("\nPattern 34\n")
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        for j in range(2*n-2*i):
            print(" ",end=" ")   
        for j in range(1,i+1):
            print(j,end=" ")     
        print()
pattern34(4)

