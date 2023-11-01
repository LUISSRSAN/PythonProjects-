#import array

#array1 = array.array('i')


#print(array)
#array2 = array.array('i',[1,2,3,4])
#print (array2)

#array2.insert(0,6)
#print(array2)


from arrays.arraypractice import *
arr1 = array('i',[1,2,3,4,5,6])

def traverseArray(array):
    for i in array:
        print(i)
# time and space complexity o(n)

traverseArray(arr1)

def accessElement(array,index):
    if index > len(array):
        print("There is not an element at this index")
    else:
        print(array[index])

accessElement(arr1,2)
# o(1) constant time complexity

def linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            print("found target")
            return i
    return -1

arr1.remove(1)
def removeElement(array,index):


#import numpy as np

#np_array = np.array([],dtype=int)
#print(np_array)

#np_array1 = np.array([1,2,3,4])
#print(np_array1)



