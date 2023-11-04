def input_employee_data():
    employee_data = {}
    while True:
        name = input("Введіть ім'я співробітника (або 'q' для завершення вводу): ")
        if name == 'q':
            break
        salary = float(input("Введіть заробітну плату співробітника: "))
        days_worked_input = input("Введіть кількість відпрацьованих днів: ")

        if days_worked_input == 'q':
            break
        days_worked = int(days_worked_input)

        employee_data[name] = {'salary': salary, 'days_worked': days_worked}
    return employee_data