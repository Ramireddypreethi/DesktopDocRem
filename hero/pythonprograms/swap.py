a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=int(input("enter 3 number:"))
if (a==b==c):
    print(a,b,c)
elif ((a==b)):
    if a>c:
        temp=a
        a=c
        c=temp
        print(a,b,c)
    elif(a==c):
        if a>b:
            temp=a
            a=b
            b=temp
            print(a,b,c)
    elif(b==c):
         if b>a:
            temp=b
            b=a
            a=temp
            print(a,b,c)
    else:
        print(a,b,c)
elif ((a<b) and (a<c) and (b<c)):
    print(a,b,c)
else:
    if ((a>b) and (a>c)):
        temp=a
        a=c
        c=temp
        print(a,b,c)
    elif ((b>a) and (b>c)):
        if(a>c):
            temp=a
            a=c
            c=temp
        print(a,b,c)
    elif ((c>a) and (c>b)):
        if(a>b):
            temp=a
            a=b
            b=temp
        print(a,b,c)

        