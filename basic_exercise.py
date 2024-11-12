def names():
 age= 24
 name = 'ofek'
 print("My name is: " + name + " and my age is: " + str(age))
#names()

def calc(x,y):
 sum = x+y
 print ('The sum of the numbers is: ' + str(sum))
 print('The subtraction is: ' + str(x-y))
 print('The multiplication is: ' + str(x*y))
 if(y!=0):
  print('division is: ' + str(x/y))
 else:
  print ('YOU CANT DIVIDE BY ZERO!!!')
#calc(10,5)

def swap_vars(a,b):
 print("a is: " + str(a) + " and b is: " + str(b))
 temp =a
 a=b
 b=temp
 print("Now a is: " + str(a) + " and b is: " + str(b))
#swap_vars(3,7)

def calculate_area(length,width):
 area = length *width
 print ("The area is: " + str(area))
 return area

#result = calculate_area(7,5)

def Basic_String_Operations():
 greeting = 'Hello world!'
 print("The length of the string is: " + str(len(greeting)))
 print("The first charecter is: " + greeting[0])
 print("The last charecter is: " + greeting[-1])

#Basic_String_Operations()

def String_Concatenation():
 first_name= 'Ofek'
 last_name ='Masas'
 full_name = first_name +' '+ last_name
 print(full_name)

#String_Concatenation()

def string_formatting():
 name= 'Ofek'
 age = 24
 print(f"My name is {name} and i am {age} years old")

#string_formatting()

def Upper_and_Lower():
 quote ='Chickens for KFC!!'
 print("Quote: " + quote)
 print("All upper: " + quote.upper())
 print("All lower: " + quote.lower())

#Upper_and_Lower()

def String_Slicing():
 word = 'Python'
 #charecter_list = list(word)
 print('The first 3 charecters: ' + word[0] + word[1] + word[2])
 print('The last 3 charecters: '+ word[-3] + word[-2] + word[-1])
 #print(word[-1:-len(word)-1:-1])
 print(word[::-1])
 #print(charecter_list)
 #print(charecter_list[::-1])

#String_Slicing()

def replacing_text():
 sentence= 'I love programming in Python.'
 print(sentence.replace('Python','bash'))

#replacing_text()

def Checking_Substrings(text,phrase):
 if(phrase in text):
  print(True)
 else:
  print(False)

#Checking_Substrings('The quick brown fox jumps over the lazy dog','fox')

def Creating_and_Printing_Lists():
 fruits = ['banana', 'watermellon', 'apple']
 print(fruits)
 fruits.append('peach')
 print(fruits)
 fruits.pop(0)
 print(fruits)

#Creating_and_Printing_Lists()

def Accessing_List_Elements():
 animals = ['cat', 'dog', 'rabbit', 'hamster']
 print('The first animal is: ' + animals[0])
 print('The last animal is: ' + animals[-1])
 print('The total number of animals is: ' + str(len(animals)))

#Accessing_List_Elements()

def Modifying_Lists():
 nums= [5, 10, 15, 20, 25]
 nums[1]=12
 print(nums)
 nums.append(30)
 print(nums)
 nums.pop(-1)
 print(nums)

#Modifying_Lists()

def List_Slicing():
 nums=[1,2,3,4,5,6,7,8,9,10]
 print(nums[:5:])
 print(nums[:-4:-1])
 nums.reverse()
 print(nums)

#List_Slicing()

def List_Comprehension(nums):
 squares = [i*2 for i in nums]
 print(squares)

#List_Comprehension([1,2,3,4,5,6,7,8,9,10])

def Counting_Occurrences(fruits,phrase):
  print(fruits.count(phrase))

#Counting_Occurrences(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'],'apple')

def Finding_the_Index(colors,color):
  print(colors.index(color))

#Finding_the_Index(['red', 'blue', 'green', 'yellow', 'blue'],'blue')

def List_Concatenation():
  nums1 = [1,2,3]
  nums2 = [4,5,6]
  print (nums1 +nums2)

List_Concatenation()

def Removing_Specific_Items(nums,number):
  while number in nums:
    nums.remove(number)
  return nums

print(Removing_Specific_Items([1, 2, 2, 3, 4, 2],2))

