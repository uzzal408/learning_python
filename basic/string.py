#asign multiline string
a = """ Hello, I am Ismail Hossen
Working In Aamra Infotainment Ltd
I have 3 years experience in PHP Laravel
Now Trying to working on python"""
print(a)

#Loop on string


for ba in "banana":
	print (ba)

#String Lenngth

b = "Hello world"
print(len(b))

# check phrase, word or character  exist in string

print("Ismail" in a)

if "Ismail" in a:
	print("Yes, Ismail is exist in variable a")

if "Django" not in a:
	print("No, Djnago is not exist in variable a")

#get string from position 2 to 5
print(b[2:5])

#get string from first ot 5
print(b[:5])
#get string from last 5
print(b[5:])

#String Format
#This is error
#age   = 10
#text = "I am a error" +age
#print(text)

# to use variable in text we need to use python format
text = "I am Ismail Hossen, I am {} years Old. I read in class {}"
print(text.format(27,12))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

text2 ="I want to pay {2} dollars for {0} pieces of item {1}."
quantity = 3
itemno = 246
price = 100
print(text2.format(quantity,itemno,price))


	

