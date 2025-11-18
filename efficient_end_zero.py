
my_nums=[1,0,2,3,0,4,5,6]
count=0

for i in range(len(my_nums)):
    if my_nums[i]!=0:
        my_nums[count]=my_nums[i]
        count+=1
print(count)
while count<len(my_nums):
    my_nums[count]=0
    count+=1
   
print(my_nums)    