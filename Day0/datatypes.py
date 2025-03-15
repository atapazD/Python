#using len with numbers gives a type error 
#print(len(23455))

#data types

#String
print("Hello"[0]) #this refers to the index of the string H-0 E-1 L-2 L-3 O-4
"123" # is not treated as a number, treated like any other string

#integer

123 + 345 #whole numbers

1234556789 # large numbers typically written with commas
print(123_456_789) # using underscore allows to split large numbers and python will ignore them and still read it as example above

#Float
3.14567 # numbers with decimal points

#boolean
True
False

#type checking/conversion
num_char = len(input("what is your name?"))
print(type(num_char)) #type function checks the data type

newNum_Char = str(num_char) # str() function converts the data type to a string
print(type(newNum_Char))

a = float(123) #float() converts data into a decimal based number
print(type(a))

# using floor type division allows you to perform division strictly returned as integer
print(type(5//2))
