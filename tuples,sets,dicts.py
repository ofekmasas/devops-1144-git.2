def Creating_and_Accessing_Tuples():
 my_tuple = (1,2,3)
 print(my_tuple)
 print(my_tuple[1])

#Creating_and_Accessing_Tuples()

def Tuple_Packing_and_Unpacking():
 person=('ofek',50,'holon')
 name,age,city = person
 print('age is: ' + str(age))
 return (name)

#print(Tuple_Packing_and_Unpacking())

def nested_tuple():
 my_tuple = ((1,2,3),(4,5,6))
 print(my_tuple[1][1])

#nested_tuple()

def tuple_methods():
 numbers = (1, 2, 3, 2, 4, 2)
 print("The number 2 appears " + str(numbers.count(2)) + " times.")
 print('The first occurrence of 3 is in the position ' + str(numbers.index(3)))

#tuple_methods()

def Creating_and_Accessing_Dictionaries():
 student = {'name':'ofek','age':24 ,'grade':100}
 print(student)
 print("The name of the student is " + student['name'])
 student['school'] = 'sela'
 print(student)
 student['age'] = 25
 print(student)
 student.pop('grade')
 print(student)
 if 'grade' in student:
  print("The grade is in the dictionary")
 else:
  print("The grade is NOT in the dictionary")

#Creating_and_Accessing_Dictionaries()

def Iterating_Over_Dictionaries():
 capitals = {'France': 'Paris', 'Spain': 'Madrid', 'Japan': 'Tokyo'}
 for x,y in capitals.items():
  print(f"The capital of {x} is {y}")
 print(f"The items are: {list(capitals.items())}")
 print(f"The keys are: {capitals.keys()}")
 print(f"The values are: {capitals.values()}")
 print(f"The capital of Germany is: {capitals.get('Germany','Not FOUOUOUOUND')} ")

#Iterating_Over_Dictionaries()

def Counting_Characters(word):
 output = {}
 for char in word:
  if(not char in output):
   output[char] = 0 #counter
  output[char]+=1
 return output

#print(Counting_Characters('helloll'))
