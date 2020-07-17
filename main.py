list1= ['physics', 'chemistry', 1997,2000]

#everything except the last element
print(list1[:-1])

#only the last element
print(list1[-1:])

#Changing value of index 2
list1[2] = 'new_value'
print(list1)

#checking the length
print(len([1,2,3]))

#concatenation
list2 = ['a','b','c']
list3 = [1,2,3]
print(list2 + list3)

#repitition
print (list2 * 4)

#check for membership
print ('d' in list2)

#Iteration
#letter represent every object in the sequence
for letter in list2:
  print (letter)

#slicing
print(list2[0:])

#Built in List Operations

#Compare sequences
print(list2 == ['a' , 'b', 'c'])

#Check the length
len(list2)

#Check for the max
print(max([234342,234234,2343243]))

#Check for the min
print(min([234342,234234,2343243]))

#Conversion of string into list
my_string = " hello hello hello"
print(list(my_string))

subjects = ['geography', 'math' , 'writing', 'lunch']

#append
subjects.append("Chemistry")

print(subjects)

#compile
#Check the occurences of an object
print(my_string.count('l'))

#extend
#add contents from another sequence
subjects.extend([101,300,200,1010])
print(subjects)

#Index
#find the lowest index with object
print(my_string.index('h'))
print(my_string[1])

#insert
#add to particular index
subjects.insert(0 ,"comp-sci")
print(subjects)

#property
#removes and returns the object from the list
subjects.pop()
print(subjects)

#remove a particular object
subjects.remove('lunch')
print (subjects)

#reverse 
#reverse a sequence
list3=[5,2,8,3]
list3.reverse()
print (list3)

#sorted
#define a comparison func
list3.sort()
print(list3)

#Ranges
print(list(range(0,1000,5)))

for x in range(3):
  print("hello")







