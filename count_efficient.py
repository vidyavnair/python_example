def cal_num(my_str):
    dict1={}
    for items in my_str:
         dict1[items]=dict1.get(items,0)+1
    return dict1
print(cal_num('vidyaavnair'))     
