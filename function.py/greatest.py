def greatest(a,b,c):
    if a>b and a>c :
        print("a is greater:")
        return a
    elif b>a and b>c :
        print("b is greater:")
        return b
    else:
        print("c is greater:")
    

a =int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c =int(input("enter the value of c:"))
result=greatest(a,b,c)
print(result)