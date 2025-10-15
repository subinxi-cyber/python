def sum(a):
    sum=0
    while(a>0):
        d=a%10
        sum=sum+d
        a=a//10
    print("the sum is",sum)
a=int(input("enter two or more  digit  number:"))
result=sum(a)
