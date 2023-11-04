import data_input
import salary_calculator
import employees_matrix
import recursion

employee_data = data_input.input_employee_data()
for name, data in employee_data.items():
    salary = salary_calculator.calculate_monthly_salary(data['salary'], data['days_worked'])
    bonus = salary_calculator.calculate_bonus(data['salary'], data['days_worked'])
    print(f"{name}: Зарплата за місяць - {salary}, Бонус - {bonus}")

employee_matrix = employees_matrix.create_employee_matrix()
employee_matrix = employees_matrix.calculate_matrix_bonuses(employee_matrix)

print("Матриця співробітників з бонусами:")
for employee in employee_matrix:
    print(employee)

print("Всі співробітники:")
recursion.print_all_employees(employee_matrix)

name_to_find = input("Введіть ім'я співробітника для пошуку: ")
found_employee = recursion.find_employee_by_name(employee_matrix, name_to_find)
if found_employee:
    print(f"Співробітник з ім'ям '{name_to_find}' знайдений.")
else:
    print(f"Співробітник з ім'ям '{name_to_find}' не знайдений.")