import time
import random

def maturity():
    age=int(input("HOW OLD ARE YOU?!?!"))
    if(age>=18):
        print('you are mature')
    elif(age>=16):
        print('almost there!')
    else:
        print('your a kid')

#maturity()

def Even_or_Odd():
    num=int(input('enter a number'))
    if num%2==0:
        print('the number is even')
    else:
        print('the number is odd')
    
#Even_or_Odd()

def Grading_System():
    grade=int(input('enter a grade'))
    if grade>100 or grade <0:
        print('invalid grade')
    elif grade>=90:
        print('grade A')
    elif grade>=80:
        print('grade B')
    elif grade>=70:
        print('grade C')
    elif grade>=60:
        print('grade D')
    else:
        print('grade F')

#Grading_System()

def positivity():
    num=int(input('enter a number'))
    if num>0:
        print('the number is positive')
    elif num<0:
        print('the number is negative')
    else:
        print('the number is zero')

#positivity()

def Eligibility_for_Discount():
    age= int(input('enter your age '))
    is_student=input("are you a student? please enter 'y' or 'n' ")
    if age<18:
        print('you are eligible for a discount!')
    elif is_student=='y':
        print('you are eligible for a discount!')
    else:
        print('you are NOT eligible for a discount!')

#Eligibility_for_Discount()

def Counting_with_a_For_Loop():
    for i in range(2,11,2):
        print(i)

#Counting_with_a_For_Loop()


def Summing_Numbers():
    sum =0
    for i in range(1,101):
        sum+=i
    print(f"the result is: {sum}")
          
#Summing_Numbers()

def Multiplication_Table():
    num =int(input('enter a number '))
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")

#Multiplication_Table()

def Countdown_with_while_Loop():
    for i in range(10,0,-1):
        print(i)
        time.sleep(1)
        
#Countdown_with_while_Loop()

def Guess_the_Number_Game():
    random_number=random.randint(1,10)
    user_number=int(input('Guess the number!'))
    while user_number != random_number:
      if user_number>random_number:
          print("too high! try again ")
      else:
          print("too low! try again ")
      user_number=int(input('Guess the number!'))
    print('congratulations! you guessed the number!')

#Guess_the_Number_Game()

def Sum_of_Positive_Numbers():
    sum=0
    num=int(input('please enter a number'))
    while num>0:
        sum +=num
        num=int(input('please enter a number'))
    print(f'the sum is: {sum}')

#Sum_of_Positive_Numbers()

def Function_with_Parameters(name):
    print(f"hello {name}!!")

#Function_with_Parameters('menahem')

def square_func(num):
    return(num*num)

#print(square_func(7))
