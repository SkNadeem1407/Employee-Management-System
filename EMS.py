class Employee:
    def __init__(self,emp_id, name, age, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.department = department
        self.designation = designation
        self.salary = salary

    def compute_final_salary(self):
            bonus = self.salary*0.05
            return self.salary + bonus


    def display_employee_details(self):
        print(f"emp Id: {self.emp_id},  name: {self.name}, age: {self.age}, department: {self.department}, designation: {self.designation}, salary: {self.salary}, Final salary: {self.compute_final_salary()} ")


class Manager(Employee):
     def display(self):
        self.display_employee_details()

     def compute_final_salary(self):
            bonus = self.salary*0.10
            return self.salary + bonus
     

class EmployeeManagementSystem:

        def __init__(self):
             self.employees = []

        def add_employee(self,employee):
             self.employees.append(employee)
             print("Employee added Successfully")

        def display_employees(self):
             if not self.employees:
                  print("No Employees are not availabe here")
             else:
                  for employee in self.employees:
                      employee.display_employee_details()

        def search_employee(self,emp_id):
             for employee in self.employees:
                  if employee.emp_id == emp_id:
                       employee.display_employee_details()
                       return
        print("Not Found")


        def update_employee(self,emp_id):
             for employee in self.employees:
                  if employee.emp_id == emp_id:
                       employee.name = input("Enter new employee name: ")
                       employee.age = int(input("Enter new employee age: "))
                       employee.department = input("Enter new employee department: ")
                       employee.designation = input("Enter new employee designation: ")
                       employee.salary = float(input("Enter new employee salary: "))
                       print("Updated Successfully")
                       return
        print("Not Updated")


        def delete_employee(self,emp_id):
             for employee in self.employees:
                  if employee.emp_id == emp_id:
                       self.employees.remove(employee)
                       print("Employee removed Successfully")
                       return
        print("Not Removed")



ems = EmployeeManagementSystem()

while True:
     print("Employee Management System")
     print("1. Add Employee")
     print("2. Add Manager")
     print("3. Display Employee")
     print("4. Search Employee")
     print("5. Update Employee")
     print("6. Delete Employee")
     print("7. The End")

     choice = input("Enter the Choice from the above Options:  ")
     if choice == '1':
          emp_id = input("Enter the employee ID: ")
          name = input("Enter the employee name: ")
          age = input("Enter the employee age: ")
          departmemt = input("Enter the employee department: ")
          designation = input("Enter the employee designation: ")
          salary = int(input("Enter the employee salary: "))
          emp1 = Employee(emp_id,name,age,departmemt,designation,salary)
          ems.add_employee(emp1)
    
     elif choice == '2':
            emp_id = input("Enter the manager ID: ")
            name = input("Enter the manager name: ")
            age = input("Enter the manager age: ")
            departmemt = input("Enter the manager department: ")
            designation = input("Enter the manager designation: ")
            salary = int(input("Enter the manager salary: "))
            man1 = Manager(emp_id,name,age,departmemt,designation,salary)
            ems.add_employee(man1)

     elif choice == '3':
          ems.display_employees()

     elif choice == '4':
          emp_id = input("Enter the employee id to search: ")
          ems.search_employee(emp_id)

     elif choice == '5':
          emp_id = input("Enter the employee id to update: ")
          ems.update_employee(emp_id)
     
     elif choice == '6':
          emp_id = input("Enter the employee id to delete: ")
          ems.delete_employee(emp_id)

     elif choice == '7':
          print("Thank you")
          break


     else:
          print("Invalid Choice")


          

                 
             
             
        
     
     
     

    
     
     


    
