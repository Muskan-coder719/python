number=int(input("enter number of terms :"))
x,y=0,1
count=0
if number<0:
    print("please enter a positive number")
else:
    print("fibonacci sequence is :")
    while count<number :
        print(x)
        z=x+y
        x=y
        y=z
        count += 1

