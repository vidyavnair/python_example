def my_func(my_str):
    dict={}
    val=1
    for i,item in enumerate(my_str):
        for j in range(i+1,len(my_str)):
            if my_str[i]==my_str[j]:
                val+=1
        dict[item] =val
    return dict    
print(my_func('vidyaa') )              