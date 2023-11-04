def print_all_employees(matrix):
    for employee in matrix:
        if isinstance(employee, list):
            print_all_employees(employee)
        else:
            print(employee)

def find_employee_by_name(matrix, name):
    for employee in matrix:
        if isinstance(employee, list):
            found_employee = find_employee_by_name(employee, name)
            if found_employee:
                return found_employee
        elif employee == name:
            return employee
    return None