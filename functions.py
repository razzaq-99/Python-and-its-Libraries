                      
                                    # Functions in Python
                                    
# def calmean(a,b):
#       mean = (a*b)/(a+b) 
#       print(mean)       
                               


# def isGreater(a,b):
#     if(a>b):
#      print("First number is greater")
#     elif(a==b):
#         print("Both numbers are equal")
#     else :
#      print("Second number is greater than first or equal") 
    


# a = 12
# b = 22
 
# isGreater(a,b)
# calmean(a,b)                                

# x = 33
# y = 11

# isGreater(x,y)
# calmean(x,y)

# K = 56
# L = 56

# isGreater(K,L)
# calmean(K,L)






# def avg(a=10,b=22):
#     print("The average of two numbers is ",(a+b)/2)
    

# avg()
# avg(3,3)
# avg(33,44)    
# avg(10)
# avg(10,0)
# avg(0,0)





# def avg(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
#         print("the avg is ", sum/len(num))

# avg(32,34)        




# def avg(*num):
#     sum = 0
#     for i in num:
#         sum = sum + i
#         return  sum/len(num)


# cal = avg(12,33)   
# print(cal)





# Built-in functions in Python

# integer = -20  
# print('Absolute value of -20 is:', abs(integer))  

# floating = -20.83  
# print('Absolute value of -20.83 is:', abs(floating))  




# def calculateAddition(n):  
#   return n+n  
# numbers = (1, 3, 4, 9)  
# result = map(calculateAddition, numbers)  
# print(result)  
  
# # converting map object to set  
# numbersAddition = set(result)  
# print(numbersAddition)  




# def filterdata(x):  
#     if x>5:  
#         return x  
 
# result = filter(filterdata,(1,2,6,9,77,0))  
 
# print(list(result))  




# small = min(11,33,44,55,66,77,88,99,00)
# print(small)




# large = max(11,22,33,44,55,66,77,88,99,00)
# print(large)




# def greatest(val1,val2,val3):
#     if(val1>val2 and val1>val3):
#         print(val1," is the greatest number")
#     elif(val2>val1 and val2>val3):
#         print(val2," is the greatest number")  
#     else:
#         print(val3," is the greatest")      

# greatest(12,22,4)
# print("done")       




# def sqRT():
#     l=[]
#     for i in range(1,31):
#         l.append(i**2)
    
#     return l


# print(sqRT())    





# def add(numbers):
#     total = 0
#     for i in numbers:
#         total += i  # or total = total+1
       
#     return(total)    

# print(add([11,22,33]))
# print(add([66,22,22]))




