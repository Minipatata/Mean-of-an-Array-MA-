import array as arr
b=arr.array('i',[2,4,-6,8,-3])
sum=0
for i in range(len(b)):
    sum=sum+b[i]
print((sum/len(b)))
