#asigning list

list1 = ['apple','banana','orange','mango','blackberry']
print(type(list1))
print(list1)

#get length of a list
print(len(list1))

#create a list using list constructor

list2 = list(('Juice','ice-cream',True,'43'))
#accessing list

print(list2[0])
#negetive indexing
print(list2[-1])

#Range of index
print(list1[2:5])
print(list1[:2])
print(list1[2:])

#check if exist any value

if "apple" in list1:
    print('Yes,Apple is exist in list2')

#change the value of list in specific index

list1[1] = "Pineapple"
print(list1)

#change a range of value

list1[2:4] = ["change item 1",'change item 2']
print(list1)

#loop throgh list

for li in list1:
    print(li)

## print item refering their index

for li in range(len(list1)):
    print(list1[li])

#Print all items, using a while loop to go through all the index numbers

i=0
while i<len(list1):
    print(list1[i])
    i = i+1

#list comprehension

new_list = [x for x in list1 if "p" in x]
print(new_list)
