#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression
x = lambda a:a*10
print(x(5))

#Multiply argument a with argument b and return the result

y = lambda a,b,c:a+b+c
print(y(10,15,5))

#Example of lambda inside function

def my_func(n):
    return lambda a:a*n
my_double = my_func(2)
print(my_double(35))

my_triple = my_func(3)
print(my_triple(50))

