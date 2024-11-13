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

def Factorial_Function(n):
    if n<0:
        return('invalid input')
    if n==0:
        return 0
    
    result=1
    for i in range(n,0,-1):
        result*=i
    return result

#print(Factorial_Function(5))

def find_max(nums):
    max=nums[0]
    for i in nums:
        if i>max:
            max=i
    return max

#print(find_max([1, 5, 3, 9, 2,12,-56,933]))

def celsius_to_fahrenheit(celsius):
    Fahrenheit = celsius*(9/5)+32
    return Fahrenheit
#print(celsius_to_fahrenheit(24))

def is_palindrome(word):
    i=0
    k=1
    while i<len(word):
        if word[i] !=word[i-k]:
            return('NOT palindrome')
        k+=2
        i+=1
    return('is palindrom')

#print(is_palindrome('lololo'))

def Sum_of_List(nums):
    sum=0
    for i in nums:
        sum +=i
    return sum
#print(Sum_of_List([10, 20, 30, 40]))

def is_prime(number):
    for i in range(2,number):
       if(i>number/2):
         return('is prime') 
       if number%i==0:
          return('is not prime')
    return('is prime')

#print(is_prime(8191))

def Simple_Calculator(a,operator,b):

    if operator =='+':
        return (a+b)
    elif operator=='-':
        return (a-b)
    elif operator=='*':
        return (a*b)
    elif operator=='/':
        if b!=0:
            return (a/b)
        else:
            return ('YOU ARE NOT ALLOWED TO DIVIDE BY ZERO!!!')
        
#print(Simple_Calculator(50,"+",5))


