#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
#Return an iterator from a tuple, and print each value:
mytuple = ("Apple","Mango","Blackberry","Dragon Fruit","Strawberry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

#String also an iterable

string1 = "Banana"
strit = iter(string1)
print(next(strit))
print(next(strit))
print(next(strit))

#Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:  #condition to stop iteration
            x = self.a
            self.a+=1
            return x
        else:
            raise StopIteration

number = MyNumber()
myiter = iter(number)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for x in myiter:
    print(x)




