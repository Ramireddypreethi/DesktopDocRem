def fib(n,a,b):
    print(a," ",b)
    c=a+b
    print(" ",c)
    a=b
    b=c
a,b=0,1
n=int(input())
fib(n,a,b)
