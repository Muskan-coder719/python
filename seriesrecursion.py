def sum_natural(n):
    if n==0 :
        return 0
    else:
        s= sum_natural(n-1) + n 
        return s 
num=int(input("enter the number :"))
x=sum_natural(num)
print(x)


OUTPUT :
enter the number :5
15
