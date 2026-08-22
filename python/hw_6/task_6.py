user_input_1 = input("Введите первое число: ")
user_input_2 = input("Введите второе число: ")
operator = input("Введите оператор (+, -, *, /): ")

# check if user input is number for avoid throwing errors in the terminal
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


if is_number(user_input_1) and is_number(user_input_2):
    num_1 = float(user_input_1)
    num_2 = float(user_input_2)
    result = f"Результат: {num_1} {operator} {num_2} ="

    if operator == '+':
        print(f"{result} {num_1 + num_2}")
    elif operator == '-':
        print(f"{result} {num_1 - num_2}")
    elif operator == '*':
        print(f"{result} {num_1 * num_2}")
    elif operator == '/':
        print(f"{result} {num_1 / num_2}")
    else:
        print(f"Вы ввели не корректрый оператор: {operator} не соответствует ни одному из доступных операторов(+, -, *, /)")
else:
    print("Не корректные символы. пожалуйста, используйте для ввода только цифры")





    
