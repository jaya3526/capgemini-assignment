	#	Class and Object
#•	1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.
class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
        
    def display(self):
        print(f"name : {self.name} , id :{self.id} ,department : {self.department}")
    
name=input("enter name = ")
id=input("Enter employee id = ")
department=input("enter employee separtment =")
employee=Employee(name,id,department)
employee.display()

#•	2. Design a `BankAccount` class with `deposit()` and `withdraw()` methods. Implement logic to prevent overdraft.
class BankAccount:
    balance = 0
    def deposite(self,money):
        BankAccount.balance+=money
        print(f"Balance in account is = {BankAccount.balance}")
    def withdraw(Self,money):
        if BankAccount.balance < money:
            print("Balance is insufficient ")
        else:
            BankAccount.balance -= money
            print(f"Balance in account is = {BankAccount.balance}")
            
bankAccount=BankAccount()
bankAccount.deposite(1000)
bankAccount.withdraw(1234)


#•	3. You are building a Library Management System. Create a `Book` class with properties like `title`, `author`, and `isbn`. Write a method to display book details.
class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn
        
    def display(self):
        print(f"Book details are title :{self.title} , author : {self.author} , isbn:{self.isbn}")
        
book=Book("being positive","ani",2)
book.display()
        
#•	4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        
    def details(self):
        print(f"student details are name :{self.name} , roll number :{self.roll_number}")
        
student=Student("Jaya sree" , "5k0")
student.details()
        
#•	5. Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
        
    def chack_availability(self,quantity):
        if self.stock >= quantity:
            print("Book is available in stack")
        else:
            print("Stock is not available")
            
product=Product("ncrt book",120,2)
product.chack_availability(3)


# Inheritance (Multiple, Multi-Level)
#•	6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year
        
    def detailsV(self):
        print(f"vehicle brand : {self.brand} ,model : {self.model} , year:{self.year}")
        
class Car(Vehicle):
    def __init__(self,seatingCapacity,trunkSize,brand,model,year):
        super().__init__(brand,model,year)
        self.seatingCapacity=seatingCapacity
        self.trunkSize=trunkSize
    def detailsC(self):
        print(f"seatingCapacity : {self.seatingCapacity} , trunkSize : {self.trunkSize}")
        
class Bike(Vehicle):
    def __init__(self,type,brand,model,year):
        super().__init__(brand,model,year)
        self.type=type
    def detailsB(self):
        print(f"bite type is {self.type}")
        
class ElectricCar(Car):
    def __init__(self,chargingTime,seatingCapacity,trunkSize,brand,model,year):
        super().__init__(seatingCapacity,trunkSize,brand,model,year) 
        self.chargingTime=chargingTime
        
    def detailsE(self):
        print(f"chargingTime for electric car : {self.chargingTime}")
        
car=Car(4,"4 x 4 size","tata","motors",2004)
car.detailsC()
car.detailsV()

bike=Bike("sports" , "Yamaha" , "R15" ,2001)
bike.detailsB()
bike.detailsV()

electricCar=ElectricCar("20 mins" , 4,"3 x 4 size" ,"toyota" ,"camry" , 2016)
electricCar.detailsE()
electricCar.detailsC()
electricCar.detailsV()
        
#•	7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.
class Person:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def detailsP(self):
        print(f"person name is {self.name}  age is {self.age}")
        
class Employee(Person):
    def __init__(self,salary,role,name,age):
        super().__init__(name,age)
        self.salary=salary
        self.role=role
    def detailsE(self):
        print(f"employee details are salary : {self.salary} , role is {self.role}")
        
class Manager(Employee):
    def __init__(self, salary, role, name, age):
        super().__init__(salary, role, name, age)   
    def approve_leave(self):
        print("Leave is approved by manager")

manager=Manager(20000,"SDE","John",23)
manager.approve_leave()
manager.detailsP()
manager.detailsE()
             
#•	8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.	
class Animal:
    def speak(self):
        pass
class Cat(Animal):
    def speak(self):
        print("cat speak like meo meo") 
class Dog(Animal):
    def speak(self):
        print("Dog Bark as bow bow")
        
cat=Cat()
cat.speak()

dog=Dog()
dog.speak()

#•	9. Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `defAirplane`. Handle potential conflicts in the `move()` method.
class FlyingCar:
    def fly(self):
        print("this method will not override")
    def move(self):
        print("it move in air")
class Car(FlyingCar):
    def move(self):
        print("it will move on land")
class DefAirplain(FlyingCar):
    def move(self):
        super().fly()
        print("it will also move in air like fliy car")
        
defAirplain=DefAirplain()
defAirplain.move()

#•	10. Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. Demonstrate method overriding and attribute reuse.
class Electronics:
    def __init__(self,color):
        self.color=color
    def displayE(self):
        print(f"electronic device color is : {self.color}")
        
class MobileDevice(Electronics):
    def __init__(self, color ,price):
        super().__init__(color)
        self.price=price
    def displayM(self):
        super().displayE()
        print(f"details of mobile device are price : {self.price} , color is {self.color}")
        
class SmartPhone(MobileDevice):
    def displayS(self):
        super().displayE()
        super().displayM()
        print(f"device color : {self.color} , price :{self.price}")
       
phone=SmartPhone("black",1000)
phone.displayS() 


#Polymorphism
#•	11. Create a class `Logger` with a method `log(message)`. Implement method overloading to log different message types (`error`, `warning`, `info`).
class Logger:
    def log(self,**kwargs):
        if "erorr" in kwargs:
            print(f"error is {kwargs["error"]}")
        if "warning" in kwargs:
            print(f"error is {kwargs["warning"]}")
        if "info" in kwargs:
            print(f"error is {kwargs["info"]}")
logger=Logger()
logger.log(error="value error",warning="dont use method here",info="this is just info")    

#•	12. Write a `Payment` class with a method `process_payment()`. Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
class Payment:
    def process_payment(self):
        print("can process payment through different payment methods")

class CreditCardPayment(Payment):
    def process_payment(self,card):
        print("Payment throught",card)
        
class PayPalPayment(Payment):
    def process_payment(self,card):
        print("payment throught ",card)
  
class BitcoinPayment(Payment):
    def process_payment(self,card):
        print("payment throught ",card)

bitcoin=BitcoinPayment()
bitcoin.process_payment("credit card")

paypal=PayPalPayment()
paypal.process_payment("PayPal Payment")

creditcard=CreditCardPayment()
creditcard.process_payment("Bitcoin Payment")

#•	13. Develop a `Shape` class with a method `area()`. Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
class Shape:
    def area(self):
        pass
    
class Square(Shape):
    def __init__(self,length):
        self.length=length
        
    def area(self):
        print(f"area of square is {self.length * self.length}")
        
class Triangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self):
        print(f"area of rectangle is {0.5*self.width*self.height}")
        
square=Square(2)
square.area()

triangle=Triangle(3,4)
triangle.area()
#•	14. Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
class Notification:
    def send(self):
        pass
    
class EmailNotification(Notification):
    def send(self):
        print("email notification send")
        
class SMSNotification(Notification):
    def send(self):
        print("sms notification send")
        
email=EmailNotification()
email.send()

sms=SMSNotification()
sms.send()
#•	15. Write an example where `Operator Overloading` is used to concatenate two `Book` objects, treating them as a series.

 

#Interface (Using Abstract Base Classes - ABC)
#•	16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_area():
        pass
    
class Rectangle(IShape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def calculate_area(self):
        print(f"area of rectangle is {self.width * self.height}")
       
class Circle(IShape):
    def __init__(self,rad):
        self.rad=rad
    def calculate_area(self):
        print(f"area of circle is {3.14*self.rad * self.rad}")
        
rectangle=Rectangle(3,4)
rectangle.calculate_area()

circle=Circle(2)
circle.calculate_area()       
#•	17. Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert():
        pass
    @abstractmethod
    def update():
        pass
    @abstractmethod
    def delete():
        pass
    
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print("we use insert command to insert in mysql database")
    def update(self):
        print("we use  alter method for sql")
    def delete(self):
        print("drop,delete and truncate used to delete in mysql")
        
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print("we use insert command to insertmany in nosql database")
    def update(self):
        print("we use  updateone method for sql")
    def delete(self):
        print("deleteone,deletemany used to delete in mysql")

sql=SQLDatabase()
sql.insert()
sql.update()
sql.delete()

nosql=NoSQLDatabase()
nosql.insert()
nosql.update()
nosql.delete()
#•	18. Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. Create a `BasicCalculator` class that implements these methods.
from abc import ABC,abstractmethod
class ICalculate(ABC):
    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
    
class BasicCalculator(ICalculate):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(f"addidtion of {self.a} , {self.b} = {self.a+self.b}")
    def subtract(self):
        print(f"subtraction of {self.a},{self.b} = {self.a - self.b}")
    def multiply(self):
        print(f"multiplication of {self.a},{self.b} = {self.a * self.b}")
    def divide(self):
        print(f"division of {self.a},{self.b} = {self.a / self.b}")
        
cal=BasicCalculator(3,4)
cal.add()
cal.subtract()
cal.multiply()
cal.divide()

#•	19. Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. Implement it in `Car`, `Bike`, and `Truck` classes.
from abc import ABC,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine():
        pass
    @abstractmethod
    def stop_engine():
        pass
    
class Car(IVehicle):
    def start_engine(self):
        print("car was started")
    def stop_engine(self):
        print("car was stoped")
        
class Bike(IVehicle):
    def start_engine(self):
        print("bike was started")
    def stop_engine(self):
        print("bike was stoped")
        
class Truck(IVehicle):
    def start_engine(self):
        print("Truck was started")
    def stop_engine(self):
        print("Truck was stoped")
        
car=Car()
car.start_engine()
car.start_engine()

bike=Bike()
bike.start_engine()
bike.stop_engine()

truck=Truck()
truck.start_engine()
truck.stop_engine()

#•	20. Write a scenario where a `UserAuthentication` interface contains `login()` and `logout()` methods, and it is implemented by `GoogleAuth` and `FacebookAuth` classes.
from abc import ABC,abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login():
        pass
    @abstractmethod
    def logout():
        pass
    
class GoogleAuth(UserAuthentication):
    def login(self):
        print("login through google")
    def logout(self):
        print("logout through google")
        
class FacebookAuth(UserAuthentication):
    def login(self):
        print("login through facebook")
    def logout(self):
        print("logout through facebook")

googleAuth=GoogleAuth()
googleAuth.login()

facebookAuth=FacebookAuth()
facebookAuth.logout()