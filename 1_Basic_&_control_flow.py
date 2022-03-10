# this is a comment
# python interpreter >>>

#variable in Python
num_1 = 38
num_2 = 10.5
num_3 = num_1 + num_2
print(num_3)
type(num_2)

#String in Python
#pythons strting is non-mutable means string element cannot be changed
country = "Bangladesh"
print(country)
type(country)
print(country[0])
print(country(1))
print(len(country))   # String length or country.__len__()
country = "Bangla" + "desh" # string concatanation
print(country.find("Bangla")) #find something from string
print(country.find("abc")) #if not found python string gives -1
print(country.replace("Bangladesh", 'bangladesh'))  #new copy of country string
str = " bcd  "
print(str.strip())  #remove space from full string
print(str.lstrip())  #remove space from leftside of string
print(str.rstrip())  #remove space from rightside of string
str1 = "AbcDeF"
str1.upper() #Uppercase
str1.lower() #Lowercase

str2 = "United"
str3 = "States"
print(str2, str3)
str2, str3 = str3, str2 #variable swapped
print(str2, str3)

#how to reverse a string in python
  # in order to make a string reversed in python 
  # you have to use the slicing as following

string = "racecar"
print(string[::-1])
#reverse the words in a string python
string = 'hello people of Bangladesh'
words = string.split()   #converts string into list
print(words[::-1])

#list/array in Python
  #list is mutable in python means item can be changed
li = ['laptop', 'watch', 'mug', 'monitor', 'moneybag']
print(li)
type(li)
print(len(li))
print(li[0])
print(li[3])
print(li[-1])
print(li[-2])
print(li[-3])
print(li[-4])
print(li[-5])
print(li[-6])

li2 = ['laptop', 100, 3.5, "BD"]
#sublist
print([li[0:3]])  
print(li[1:3])
print(li[-1:])  
print(li[-1:1])
print(li[:-1])
print(li[0:4:2]) 
print(li[0:4:1])
print(li[0:4:2])
print(li[::1])
print(li[::2])
print(li[::-1]) # list reverse

li3 = li2 + ["pencil", 5]
print(li3)

#Conditional Logic in Python
  #boolean values : true/false
print(type(True))
print(type(False))

print(bool(0))  #false
print(bool(1))  #true
print(bool(-1)) #true

print(bool"string") #true
print(bool" ") #true
print(bool"") #false

print(bool[1,2,3]) #true
print(bool[]) #false
  #And or Not
a = True  #true
not a #false

b = False
print(a and b)  #false
print(a or b) #true

  #checking wheather an item is in the list or not
another_li = [1,2,3,4]
print(3 in another_li) #true
print(6 in another_li) #false

another_li2 = ['a', 'b', 'c']
print('a' in another_li2) #true
print('d' in another_li2) #false

  #if-else
a = 5
b = -3
c = 0

if a > 0:
  print("a positive")
if b > 0:
  print("b positive")
if c == 0:
  print("zero")
elif c > 0:
  print("positive")
else:
  print("nothing")

vowels = ['a' , 'e', 'i', 'o', 'u']
x = 'i'
if x in vowels:
  print("x is true so vowel")
else:
  print("x is not here so consonant")

#Loop in Python
  #While
i = 1
while i <= 10:
  print(i)
  i += 1
  #fibonacci
fib_1 = 0
fib_2 = 1
while fib_2 < 20:
  print(fib_2)
  fib_1, fib_2 = fib_2, fib_1 + fib_2

  #for(no condition)
vowels1 = ['a','e','i','o','u']
for ch in vowels1:
  print(ch)
  #range : a list that returns a number list
print(range(20))
print(range(5,20))
print(range(5,20,22))
print(range(1,100,5))

for i in range(10):
  print(i)
  #Break
for i in range(10):
  print(i)
  if i > 5:
    break
  #continue
for i in range(10):
  if i < 5:
    continue
  print(i)
  
  #for-else
