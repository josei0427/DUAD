class Employee:
    def __init__(self, name, last_name, user_id, level):
        self.name = name
        self.last_name = last_name
        self.user_id = user_id
        self.level = level

    def all_info(self):
        print(f'El nombre del empleado es: {self.name}')
        print(f'El apellido del empleado es: {self.last_name}')
        print(f'El usuario del empleado es: {self.user_id}')
        print(f'El nombre del empleado es: {self.level}')

class Supervisor:
    def __init__(self, team_supervised):
        self.team_supervised = team_supervised

    def sup_info(self):
        print(f'El empleado es supervisor del equipo de: {self.team_supervised}')


class EmployeeFullInfo(Employee, Supervisor):
    def __init__(self, name, last_name, user_id, level, team_supervised):
        Employee.__init__(self, name, last_name, user_id, level)
        Supervisor.__init__(self, team_supervised)

employee = EmployeeFullInfo("Chandler", "Bing", "mauriel_bing", "Tier 3", "Lan & Swithcing")
employee.all_info()
employee.sup_info()