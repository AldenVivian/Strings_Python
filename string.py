samp1='hello'
samp2 = "hello world"
samp3 = "this is also a string"

print("hello \nworld")

print("hellow \tworld")

#length of string ("len()" function)
length_string = len(samp1)
print(length_string)


my_string="Hello4World"


#Indexing
print(my_string[0])
print(my_string[7])

#Reverse Indexing(last char of string = -1)
print(my_string[-1])
print(my_string[-3])

#Slicing(sub-sections)
print(my_string[2:])
print(my_string[0:3])
print(my_string[:3])

print(my_string[2:8])

print(my_string[::])#complete string

print(my_string[::2])#step 
print(my_string[::3])

print(my_string[1:5:2])#[start:stop:step]

print(my_string[::-1])#reverse the string


#concatenate
name = "Sivian"
last_letters = name[1:]

print('V'+last_letters)

x = "Hello World"

print(x*10)

#string functions
test = "This is a test string"

print(test.upper()+"||"+test.lower())

print(test.split())
print(test.split('i'))#Th s s a test str ng



#Injecting variable into a string(".format()")

print("This is a string {}".format("INSERTED"))

print("The {2} {1} {0}".format("fox","brown","quick"))
print("The {1} {1} {1}".format("fox","brown","quick"))

print("The {q} {b} {f}".format(f='fox',b='brown',q='quick'))

res = 100/77;

print("The result was = {}".format(res))

print("The result was = {r:1.3f}".format(r=res))#{values:width.precision f}

#fstrings(formatted string)

test2 = "John"
num = 100
print(f"Hello my name is {test2}")
print(f"The number is = {num} and my name is {test2}")

#placeholder

k,l = 'one','two'

print("1 = %s and 2 = %s "%(k,l))





















