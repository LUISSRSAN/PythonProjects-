

import numpy as np

# creating 2d array using numpy
twoDArray = np.array([[11,15,10,6],
                     [10,14,11,5],
                     [12,17,12,8],
                     [15,18,14,9]])
print(twoDArray)

# insertion to 2d array
#adding column time complexity O(mn)
newTwoDArray = np.insert(twoDArray,0,[[1,2,3,4]],axis =1)
print(newTwoDArray)

#newTwoDArray2 = np.insert(newTwoDArray,0,[[1,2,3,4]],axis=0)
#print (newTwoDArray2)
#axis = 1 for first column axis = 0 for first row insertion
#adding row time complexity 0(mn)

# accessing elements of 2D ARRAY array[row][col]
print(newTwoDArray[0][4])

def accessElement(array,rowIndex,colIndex) :
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect Index")
    else:
        print(array[rowIndex][colIndex])


accessElement(newTwoDArray,2,0)

#Traversing 2D Array

def traverse2DArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse2DArray(newTwoDArray)

# searching for an element in 2D Array

def searchTDArray(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                print("found target")
                print(array[i][j])

    return "not found"

print(searchTDArray(newTwoDArray,14))

#deletion from 2d Array

newTDArray = np.delete(newTwoDArray,0,axis=0)
print(newTDArray)