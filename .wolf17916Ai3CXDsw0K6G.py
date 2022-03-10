'''
There are 4 types of python built in data structures :
  1. list/array
  2. tuple
  3. set
  4. dictionary
'''
#---------------------------------------------------------------------
# list/array --> [a,b,c, 5, 6]
  # list operations :
    #item/element access
    #looping/iterating
    #item reverse
    #sort items
    #append item
    #list extend
    #insert item in list
    #check item exists or not
    #item length, item count, item frquency, item pop
  
li  = [1,2,3,4,5,6,7,8]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.append(9)
print(li)
li.insert(0,99)
print(li)
li2 = range(10, 21)
print(li2)
li.extend(li2)
print(li)
print(li.count(9))
print(li2.count(9))
x = 5
li.remove(5)
print(li)
print(li.pop())
print(li.pop(10))
li = [0] *33
print(li)
  # difference between copy and deep copy of python : to do -> search on internet 
# using list as stack(last come first out)
stack = []
stack.append(2)
stack.append(3)
stack.append(5)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
# using list as queue (first come first out)
queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
print(queue.pop(0))
print(queue)
# list comprehension
li = range(1,31)
even = []
for item in li:
  if item%2==0:
    even.append(item)
print(even)
  #list comprehension
comprehensed_even = [item for item in li if item%2==0]
print(comprehensed_even)
#---------------------------------------------------------------------

#tuple --> (1,2,3,[4,5,6])
#tuple is not mutable/changeable
#tuple pack and unpack
t = (1,2,3)
a,b,c = t 
print(a,b,c)
x = 5
y = 8
t = x,y 
print(t)

  #creating tuple
tpl = (1,2,3, 'string', 3.5)
  #accessing/indexing tuple
print(tpl[0])
print(tpl[-1])
  #converting tuple to list
li = list(tpl)
print(li)

tpl_new = 1,2,3 #packing
print(type(tpl_new)) 

a,b,c = tpl_new  #unpacking
print(a)
print(b)
print(c)

a,b = b,a #unpacking
print(a)
print(b) 
  #looping tuple
for item in tpl:
  print(item)
'''
1. Difference between tuple and list?
    -list mutable/changeable; tuple not mutable/changeable
2. Where to use tuple?
    - in function where we need to return multiple value
'''
  #nested tuple 
tpl = (1,2,3,(10,20,30))
print(tpl[3])
  #nested list 
li = [1,2,3,[10,20,30]]
print(li[3])
#---------------------------------------------------------------------
# set --> {laptop, pen, lamp, tablet} 

  #creating set

    #empty set
a = set() #set takes only single arguements; so we have to give iterable arguements like list or tuple to make a set
print(a)
print(type(a))
    #creating set from tuple
tpl = (1,2,3,4,5,6,7)
a = set(tpl)
print(a),
print(type(a))
    #creating set from list
li = [10,20,30,40,50, 7]
b = set(li)
print(b)
print(type(b))
    #set operations
print(a & b) #set intersection
print(a | b)  #set union
print(a^b)

#---------------------------------------------------------------------
# dictionary 
