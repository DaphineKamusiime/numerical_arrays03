##programme displaying an array where the user chooses one value and its index is displkayed
from array import*
array_1=[1,2,3,4,5]
num=int(input('select one value'))
tryagain=True

if num in array_1:
    print(array_1.index(num))
else:
    print('not in array')