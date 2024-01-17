# class Employee:
#     salary = 1200
#     name = "Ahmed"
#     def empSalary(x):
#         return x.salary
    
# xyz = Employee()
# print(xyz.salary) 
# print(xyz.name)  


class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def empSalary(x):
        return x.salary+" "+x.name
        
    
xyz = Employee("Ali","120000")
# print(xyz.name) 
# print(xyz.salary) 
 
# print(xyz)      prints address
print(xyz.empSalary())


