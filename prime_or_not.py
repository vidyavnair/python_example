'''num=int(input())
for i in range(2,num-1):
    if num%i==0:
        print('not a prime number')
        break
else:
        print('prime number')'''
num=int(input())
i=2
while(i<num):
        if num%i==0:
              print('not prime')  
             
              break
        i+=1
else:
      print('prime')           