#1.ATM Simulation

balance=0
while True:
    choice=int(input(' 1.Check balance \n 2.Deposit money \n 3.withdraw money \n 4.exit \n Enter the choice =' ))
    if(choice == 1):
        print(f'balance is {balance}')
    elif(choice == 2):
        n=int(input('enter money to deposite ='))
        balance+=n
        print("money deposited successfully")
    elif(choice == 3):
        n=int(input('Money to with draw ='))
        if(balance < n):
            print(f'Insufficient balance,available balance is only {balance}')
        else:
            balance-=n
            print('payment successfull')
    else:
        break

#-------------------------------------------------------------------------------
#2.temperature conversions

#cel to for
# (0°C × 9/5) + 32 = 32°F -- for 0 deg celcious
temp=int(input('Enter temperature in celcious = '))
def celtofor(temp):
        print(int((temp*9/5)+32))
celtofor(temp)

#cel to kel
#0°C + 273.15 = 273.15K -it will take the celcious as input
temp=int(input('Enter temperature in celcious = '))
def celtokel(temp):
        print(int(temp+273.15))
celtokel(temp)

#far to cel
#(32°F − 32) × 5/9 = 0°C -- 32 deg far
temp=int(input('Enter temperature in Farhene = '))
def fartocel(temp):
        print(int((temp-32)*5/9))
fartocel(temp)

#far to kel
#(32°F − 32) × 5/9 + 273.15 = 273.15K -it will take the far value
temp=int(input('Enter temperature in Farhene = '))
def fartokel(temp):
        print(int((temp-32)*5/9 +273.15))
fartokel(temp)

#kel to cel
#0K − 273.15 = -273.1°C -- give the kel value input
temp=int(input('Enter the kelvin value ='))
def keltocel(temp):
    print(int(temp-273.15))
keltocel(temp)

#kel to far
#(0K − 273.15) × 9/5 + 32 = -459.7°F --give kel input
temp=int(input('enter the kel value ='))
def keltofar(temp):
    print(int((temp-273.15)*9/5+32))
keltofar(temp)

#-------------------------------------------------------------------------------
#3.guessing number
import random
n=random.randrange(1,100)
print(f'Random number if {n}')
guess_num=int(input('Guess the number'))
while n!=guess_num:
    if(guess_num > n):
        print('Input if Too High , Try again')
    else:
        print('Input if Too Low , Try again')
    guess_num=int(input('Guess the number'))
print('You Won the game')

#-------------------------------------------------------------------------------
#4.grade printing , taking each subject has 100 marks total
stu_name=input('Enter student name')
print('Enter marks of 5 subjects')
s=0
for i in range(0,5):
    marks=int(input(f'Enter marks of {i+1} subject'))
    s+=marks

print(f'Total marks are {s}')
percentage= (s/500)*100
print(f'percentage is {percentage} %')

if(percentage <= 34):
    print('fail')
elif(percentage > 34 and percentage<50):
    print('C grade')
elif(percentage >= 50 and percentage <= 85):
    print('B grade')
else:
    print('A grade')

#-------------------------------------------------------------------------------
#5.Shopping cart

items=[]
def add_item(val):
    items.append(val)

def view_cart():
    print(items)
    
def total_price():
    s=0
    for i in items:
        s+=i[1]
    print(f'total price in cart is {s}')
        
while True:
    choice=int(input(' 1.Add Item \n 2.View cart Item \n 3.calculate total price \n 4.exit \n Enter the choice =' ))
    if(choice == 1):
        name=input('Enter name of Item =')
        price=int(input('Enter price of item ='))
        add_item([name,price])
    elif(choice == 2):
        view_cart()
    elif(choice == 3):
        total_price()
    else:
        break
    
#-------------------------------------------------------------------------------
#6.prime numbers in a range
def prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            if(n%i==0):
                return False
        return True

a=int(input('Enter first number'))
b=int(input('Enter second number'))

for i in range(a,b+1):
    if(prime(i)):
        print(i)

#-------------------------------------------------------------------------------
#7.loan details
salary=int(input('Enter salary = '))
age=int(input('Enter age ='))
credit_score=int(input('enter credit score ='))

if salary > 100000 and age > 18 and credit_score > 1000:
    print('Loan is approved')
else:
    print('Bank loan is rejected,reasons are :')
    if(salary <= 100000):
        print('salary is <= 100000 , so loan was rejected')
    if(age <= 18):
        print('age is <= 18 , so loan was rejected')
    if(credit_score <= 1000):
        print('credit_score is <= 1000 , so loan was rejected')

#-------------------------------------------------------------------------------
#8.Multiplication table generation
n=int(input('Enter number for which table need to generate ='))
print('Enter range of table')

start=int(input('Enter from which table should start = '))
end=int(input('Enter from which table should end = '))

for i in range(start,end+1):
    print(f'{n} * {i} = {n*i}')

#-------------------------------------------------------------------------------
#9.string analysis
def vowels(ch):
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        return True
    else:
        return False
str=input('Enter lowwer string to analyse =')
ipt=str.lower()

c_v=0
c_c=0
c_special=0
c_digit=0

for i in ipt:
    if(i>='a' and i <= 'z'):
        if(vowels(i)):
            c_v+=1
        else:
            c_c+=1
    elif i>='0' and i<='9':
        c_digit+=1
    else:
        c_special+=1

print(f'no of vowels are {c_v}')
print(f'no of consonents are {c_c}')
print(f'no of special characters are {c_special}')
print(f'no of degits if {c_digit}')
print(f'reverse of string is {str[::-1]}')

#-------------------------------------------------------------------------------
#10.bill slip
totalbillamount=int(input('enter total bill ='))
noofpeople=int(input('enter no of people ='))
tip_per=int(input('Enter tip percent ='))

total=totalbillamount*tip_per/100

print(f'Amount each person should pay is {total/noofpeople}')

#-------------------------------------------------------------------------------
#11.password strength checker
password=input('enter password =')
if(len(password) >= 8 ):
    upper_letter=0
    lower_letter=0
    digit=0
    special=0

    for i in password:
        if(i >= 'a' and i<='z'):
            lower_letter+=1
        elif i>='A' and i<='Z':
            upper_letter+=1
        elif i>='0' and i<='9':
            digit+=1
        else:
            special+=1

    if upper_letter > 0 and lower_letter >0 and digit > 0 and special > 0:
        print('Password is strong')
    else:
        print('Password is not strong')
else:
    print('Password should contain at least 8 characters')

#-------------------------------------------------------------------------------
#12.generate the pattern

format=int(input('Enter which format does pattern need to print'))
n=int(input('number of lines in pattern'))

if(format == 1):
    for i in range(1,n+1):
        j=i
        while j > 0:
            print("*",end="")
            j-=1
        print()
else:
    for i in range(1,n+1):
        j=n-i+1
        while j > 0:
            print("*",end="")
            j-=1
        print()

#-------------------------------------------------------------------------------
#13.palindrome for string---if it is palindrome it will exit loop,other wise function ask user to give other input

def palindrome(str):
    j=len(str)-1
    i=0
    while(i<=j):
        if(str[i] != str[j]):
            return False
        i+=1
        j-=1
    return True

while True:
    name=input('enter name = ')
    if(palindrome(name)):
        print(f"{name} is palindrome")
        break
    else:
        print(f"{name} is not palindrome,Try again")

#-------------------------------------------------------------------------------
#14.Factorial of a number
n=int(input('Enter number for which we need to find the factorial ='))

if(n < 0):
    print("For negative number we can't find the factorial")
elif(n==0):
    print('factorial of 0 is 1')
else:
    s=1
    for i in range(1,n+1):
        s*=i
    print(f"factorial of a number if {s}")

#-------------------------------------------------------------------------------
#15.Leap year
def leapyear(n):
    if(n%4==0):
        if(n%100==0):
            return n%400==0
        return True
    else:
        return False

c=1
while c==1:
    num=int(input('Enter any number ='))
    if(leapyear(num)):
        print(f'{num} is leap year')
    else:
        print(f'{num} is not leap year')
    c=int(input('Enter 1 to contine 0 to exit  ='))

#-------------------------------------------------------------------------------
#16.Odd and Even Separator
lst=list(input('Enter list of numbers =').split(',')) #give in form of 1,2,3,4,5,6,...
# print(lst)
even=[]
odd=[]

for i in lst:
    val=int(i)
    if(val%2==0):
        even.append(val)
    else:
        odd.append(val)

print(f'Even list is {even}')
print(f'odd list is {odd}')

#-------------------------------------------------------------------------------
#17.word count
str=input('Enter string =').split(' ')
print(len(str))

#-------------------------------------------------------------------------------
#18.BMI Calculator
weight=int(input('Enter weight in KG ='))
height=float(input('Enter height in m ='))
sq_height=height*height #square root of heigh

bmi=weight/sq_height
print(f'BMI value is {bmi}')

if bmi<18.5:
    print("underweight")
elif bmi>=18.5 and bmi <25:
    print("normal weight")
elif bmi>=25 and bmi <30:
    print("over weight")
else:
    print("obesity")

#-------------------------------------------------------------------------------
#19.second largest value in list
n=int(input('enter numbers in list ='))
if(n==0):
    print('List do not contain any element')
else:
    lst=[]
    for i in range(0,n):
        p=int(input('enter number ='))
        lst.append(p)
    lst.sort()

    if(n==1):
        print(lst[0])
    else:
        print(lst[n-2])
#-------------------------------------------------------------------------------
#20.FizzBuzz Problem

for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

