def fib(n):
    count=0
    while count<n:
        if count<=1:
            print(count,end=' ')
            old=0
            new=1
        else:
            print(old+new,end=' ')
            old,new=new,old+new
        count+=1
fib(10)
