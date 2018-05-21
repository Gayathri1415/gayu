n=int(input('enter an integer'))
a=[int(x) for x in input().split()]
k=0
for i in a:
    k=0
    for j in a:
        if i==j:
            k+=1
    if k==1:
        print(i)
