from array import *

#create array
arry = array('i',[1,2,3,4,5])

#traverse array using for loop
for i in arry:
    print(i)
#access individual elements
arry[0]

#append any value
arry.append(12)
#insert value in array
arry.insert(0,13)

#extend array

arry2= array('i',[15,16])
arry.extend(arry2)

#add items from list into array

tempList = [20,21,22]
arry.fromlist(tempList)

#remove any array element
arry.remove(12)

#remove last element
arry.pop()

#fetch any element through index using index() method
print(arry.index(21))

# reverse python array using reverse
arry.reverse()

#get aray buffer information through buffer_info()
print(arry.buffer_info())

#Check for number of occurences
arry.append(11)
print(arry.count(11))

# convert array to string
print(arry.tostring())

#convert array to a python list

arry.tolist()
#append a string to char array using fromstring()

#slice elements from an array
print(arry.slice[1:4])