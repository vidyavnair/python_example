num=[1,0,2,3,0,4,5,6]

counts=num.count(0)
for _ in range(counts):
 num.remove(0)
 num.append(0)
print(num)