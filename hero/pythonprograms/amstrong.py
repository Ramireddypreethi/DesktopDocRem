
n=int(input())
n1=len(str(n))
temp=n
am=0
while n>0:
    rem=n%10
    am=am+rem**n
    n=int(n/10)
if temp==am:
    print("amstrong")
else:
    print("not amstrong")