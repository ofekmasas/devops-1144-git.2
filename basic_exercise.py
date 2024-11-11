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
 word_list = sentence.split()
 print(word_list)

replacing_text












def fibonachi(n):
 a=1
 b=1
 if(b<n):
  return ()