

integers = [1,2,3,4]

print(integers)

stringList = ["Milk","Cheese","Butter"]
print(stringList)
mixedList = [1,1.5,'spam']
print(mixedList)
nestedList = [1,2,4,5,[1.5,1.6],['test']]
empty = []
print(nestedList)

# accessing/traversing a list
shoppingList = ['Milk','Cheese','Butter']
shoppingList[0]

for i in shoppingList:
    print(i)

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList)

#Update/Insert
myList = [1,2,3,4,5,6,7]
print(myList)
myList[2]=33
print(myList)
#insert()  , append() , extend()
myList.insert(0,11)
print(myList)
myList.append(55)
print(myList)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)

#Slice/Delete
myList = ['a','b','c','d','e','f']
myList[0:2] = ['x','y']
myList.pop(1)
print(myList)

del myList[3]
print(myList)

#myList.remove('e')

#Searching for an element
my_list = [10,20,30,40,50,60,70,80,90]
target = 500
def linear_Search(p_list,p_target):
    for i,value in enumerate(p_list):
        if value == p_target:
            return i
    return -1



print(linear_Search(my_list,target))


