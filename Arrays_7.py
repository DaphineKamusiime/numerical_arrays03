##asking a user to enter values in one array and moving a value into a different array
from array import*
nums=array('i',[])
for x in range(0,5):
    num=int(input('enter an integer'))
    nums.append(num)
    nums=sorted(nums)
print(nums)
num=int(input('enter a number from the array '))
if num in nums:
    nums.remove(num)
    numz=array('i',[])
    numz.append(num)
    print(num)
    
else:
    print('not in the array')
