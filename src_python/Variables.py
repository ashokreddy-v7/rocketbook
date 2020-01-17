# Printing Variables

# Numbers
number1 = 200
number2 = 300
number3 = number1 = number2

print(number1)
print(number2)
print(number3)
print("sum=", number1+number2)

# Strings
string1 = "This is string"
string2 = """this can be a multi line string"""

print(string1)
print(string2)
print(string1[2:5]*2)
print("concat=", string1+"-concatinated to-"+string2)


# Lists

list = ['abcd', 786 , 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)
print(list[1:4])
print(list+tinylist)


# Tuples

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print(tuple)
print(tuple*3)

# Dictionaries

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(tinydict)
print(tinydict['name'])

# Sets

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)
