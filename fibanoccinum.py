a=int(input('number:'))
n1=0
n2=1
for i in range(0,a):
    sum=n1+n2
    print (sum)
    n1=n2
    n2=sum
