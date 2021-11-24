f = open("testfile.txt","a")
# print(f.read())
# for x in f:
#     print(x)

f.write("This is new line, good to see!!")
f = open("testfile.txt","r")
print(f.read())
f.close()