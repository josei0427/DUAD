list_of_keys = ['access_level', 'age']
employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
new_employee = {}
for key, value in employee.items():
    if key not in list_of_keys:
        new_employee[key] = value
print(new_employee)