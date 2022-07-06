from Employee import Employee 


employee1 = Employee("islam", 60, "facebook", True, 5, 6000)
employee2 = Employee("ali", 30, "coding", False, 3.5, 5000)


print(employee1.is_excellent())
print(employee2.is_excellent())


print(employee1.salary)
employee1.bonus()
print(employee2.salary)
employee2.bonus()