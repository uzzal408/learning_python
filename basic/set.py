#assign set

set1 = {"apple","Banna","Mango"}
print(set1)
print(type(set1))
# A set is a collection which is unorder, unchangable and unindexed
#Unchangeble but you can add and remove item from set
#Duplicate no allowed in set
set2 = {"Cricket","Soccer","Football","HandBall","Tenis","Soccer"}
print(set2)

#Accessing into set
#With For loop

for x in set2:
    print(x)

#check if Cricket present in set2

if "Cricket" in set2:
    print("Cricket is present")

#add item in set

set1.add("Oragne")
print(set1)

#add item from another set into current set use update

set1.update(set2)
print(set1)
#Any kind of iterable object like list, tuple or dictionary also can add with update function

list1 = ["Ismail","Sumon","Sajib"]

set1.update(list1)
print(set1)

#remove item using remove

#if item not existed in set remove appear erro

set1.remove("Sumon")
print(set1)

#Remove Item Using discard and discard never appear error if item does not exist
set1.discard("Sajib")
print(set1)