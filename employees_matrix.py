
def create_employee_matrix():
    matrix = []
    while True:
        name = input("Введіть ім'я співробітника (або 'q' для завершення вводу): ")
        if name == 'q':
            break
        salary = float(input("Введіть заробітну плату співробітника: "))
        days_worked = int(input("Введіть кількість відпрацьованих днів: "))
        employee = [name, salary, days_worked]
        matrix.append(employee)
        return matrix


def calculate_matrix_bonuses(matrix):
    for employee in matrix:
        name, salary, days_worked = employee
        bonus = calculate_bonus(salary, days_worked)
        employee.append(bonus)
    return matrix