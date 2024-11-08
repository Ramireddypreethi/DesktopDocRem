b1,b2,b3=499.00,855.00,645.00
print("Cost of book1(Introduction to Python Programming): Rs 499.00")
print("Cost of book2(Python Libraries Cookbook): Rs 855.00")
print("Cost of book3(Data Science in Python): Rs 645.00")
d_charges=250.00
p=0
while True:
    choice=input("enter choice:")
    if choice=='b1':
        n=int(input("enter number of b1:"))
        p=p+n*b1
        ch2=input("enter another choice:")
        if ch2=='n':
            break
    elif choice=='b2':
        n=int(input("enter number of b2:"))
        p=p+n*b2
        ch2=input("enter another choice:")
        if ch2=='n':
            break
    elif choice=='b3':
        n=int(input("enter number of b2:"))
        p=p+n*b3
        ch2=input("enter another choice:")
        if ch2=='n':
            break
    else:
        print("books not available")
print("GST:12%")
print("Delivery Charges: Rs.250.00")
amount=(p+(p*(12/100)))+d_charges
print("Total price of books:",amount)







