def iterate(n):
    for i in range(1,n+1):
        if i%2==0:
            yield (i,'even')
        else:
            yield (i,'odd')
for i in iterate(20):
    print(i)
