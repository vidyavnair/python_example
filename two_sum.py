my_data=[1,2,3,4,5,6]
target=7
dict1={}

for i,items in enumerate(my_data):
    dict1[items]=i
for i in range(len(my_data)):
    my_value=target-my_data[i]
    if my_value in dict1:
        print(my_data[i],my_value) 
    