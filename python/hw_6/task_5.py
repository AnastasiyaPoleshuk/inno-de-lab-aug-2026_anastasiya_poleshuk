import random

MIN_NUM = 1
MAX_NUM = 20
attempts_left = 5
current_attempt = 1
random_num = random.randint(MIN_NUM, MAX_NUM)

print(f"Я загадал число от {MIN_NUM} до {MAX_NUM}. У тебя {attempts_left} попыток!")

while attempts_left > 0:
    user_input = int(input(f"Попытка {current_attempt}. Введите число: "))
    attempts_left -= 1

    if user_input > random_num:
        print(f"Слишком много! Осталось попыток: {attempts_left}")
    elif user_input < random_num:
        print(f"Слишком мало! Осталось попыток: {attempts_left}")
    else:
        print("Ты угадал! Отличная работа.")
        break
    current_attempt += 1
else:
    print("хехехехе ты не угадал")