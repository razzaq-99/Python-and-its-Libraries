
                                    #1st Program in Python

# print("Hello world!!!",45,00)
# print(22+34)

# print("number ",45,566, sep=" - ")


                                    # Variables in Python
  
# a = 1234
# b = "abc"
# c = True
# list1 = [1,2,3,"Ok",22.2]
# print(a)
# print(b)
# print(c)
# print(list1)


# print(a+b)
# print(b+c)

                                      # Data types in Python
   
# print("the type of a is ", type(a))
# print("the type of b is ", type(b))
# print("the type of c is ", type(c))
# print("the type of list1 is ", type(list1))



                                # Operators and calculations in Python

# num1 = 23
# num2 = 45

# print("the addition of ",num1 , " and ", num2 , " is " , num1+num2)

# print("the subtraction of ",num1 , " and ", num2 , " is " , num1-num2)

# print("the multiplication of ",num1 , " and ", num2 , " is " , num1*num2)

# print("the division of ",num1 , " and ", num2 , " is " , num1/num2)




                                   # Type casting in Python

# from numpy import double
# a = "12"
# b = "123"
# c = 12.2
# d = "12.34"

# print(a+b)
# print(int(a)+int(b))
# print (int(c))
# print(int(c) + double(d))

# x = 1.9
# y = 2.7
# z = 3.32322

# print(x+y+z)




                                 # User Input in Python

# print("input your value ")
# var  = input("Input your value ")
# print("Your inputed value is :",var)


# x = input("Input your 1st number ")
# y = input("Input your 2nd number ")

# print(x + y)                                      # consider it as a string
# print (int(x) + int(y))                             # It will work Fine 





                                 # Strings in Python
 
# str1 = "Abdul"
# str2 = 'Ali'
# str3 = '''Hello My Name is Ahmed
# ALi and "I live in Canada
# and Pakistan" '''                             

# print(str1)
# print(str2)
# print(str3)


# print(str1[0])

# for character in str1 :
#     print(character)

# for character in str2:
#     print(character)



                   # Strings Slicing and Operations in Python
                   
# Name = 'Ahmed khan'
# print(len(Name))  

# print(Name[0:5])         #Slicing     
# print(Name[:10])
# print(Name[:3])
# print(Name[0:-4])
# print(Name[-4:-1])

# for character in Name :
    # print(character)
    
    
    
    
                        # Methods of String in Python
                        
# car = "civic 2023"

# print(len(car))      

# print(car.upper())   

# print(car.lower())   
  
# print(car.rstrip('!')) 
        
# print(car.replace("Civic","Toyota")) 

# print(car.split())

# print(car.capitalize())

# print(car.splitlines())
  
# print(car.swapcase())  

# print(car.find("c"))

# print(car.count('c'))

# print(car.endswith("2023"))

# print(car.islower())

# print(car.startswith("2023"))
    
    
    
    
    
    
                               # If else Statements in Python
                               
# age = int(input("Input your age "))
# print("Your age is ",age)                   

# if(age>18 & age<100):
#     print("You can vote")
    
# elif(age==18):
#     print("Still you can not vote")    
# else :
#     print("You can not Vote")                


# num = int(input("inter your number "))

# if(num>0):
#     print("The number is positive =",num)

# elif(num==0):
#     print("The number is zero =",num)
    
# else:
#     print("The number is negative =",num)        


import time

timestamp = time.strftime('%H:%M:%S')

print(timestamp)

# Extract hours from the timestamp and convert it to an integer
hours = int(timestamp.split(':')[0])

if hours < 12:
    print("Good Morning!")
    
elif hours < 18:
    print("Good Evening!")
    
else:
    print("Good Night")
