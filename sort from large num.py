l=[4,1,5,3,8,9,1,32,13,7]
for i in range(0,len(l)):
  for j in range(i,len(l)):
    if (l[i]<l[j]):
      l[i],l[j]=l[j],l[i]
print (l)
