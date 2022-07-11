##ask a user to enter a value between 2 and 5 that divides the array
from array import*
import math

nums=array('i',[])
nums=[15.65,24,34,36.06,58.93,74.81]
tryagain=True

num=int(input('enter a whole number between 2 and 5'))
if num>2 and num<5:
    for i in range(0,5):
        ans=nums[i]/num
        print(round(ans,2))
     
else:
    print('try again')
    
