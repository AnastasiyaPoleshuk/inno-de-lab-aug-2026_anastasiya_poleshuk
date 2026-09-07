from typing import Any


DEFAULT_RETURN_INDEX_BASE = 10.0

return_test_cases = [
    {"film_title": "Matrix", "days_overdue": 5, "fine_rate": 1.5},
    {"film_title": "Inception", "days_overdue": "пять", "fine_rate": 2.0},
    {"film_title": "Avatar", "days_overdue": 0, "fine_rate": 2.5},
    {"film_title": "Interstellar", "days_overdue": [3], "fine_rate": 3.0},
]


def calculate_overdue_fine(
    film_title: str,
    days_overdue: Any,
    fine_rate: float,
) -> tuple[float, float] | None:
    """Calculate an overdue fine and a return index safely.

    Args:
        film_title: title of film
        days_overdue: number of overdue days
        fine_rate: fine charged for one overdue day

    Returns:
        tuple that contains from total fine and return index, or None when input can't be processed
    """
    try:
        numeric_days = float(days_overdue)
        total_fine = numeric_days * fine_rate
        return_index = DEFAULT_RETURN_INDEX_BASE / numeric_days

        print(f"Фильм: '{film_title}' | Итоговый штраф: {total_fine}$ | Индекс: {return_index}")
        return total_fine, return_index
    except TypeError as error:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для '{film_title}': {error}")
    except ValueError as error:
        print(f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число для '{film_title}': {error}")
    except ZeroDivisionError as error:
        print(f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки для '{film_title}': {error}")
    finally:
        print("--- Проверка транзакции возврата завершена ---")


print("=== ПРОВЕРКА ВОЗВРАТОВ ===")

for case in return_test_cases:
    calculate_overdue_fine(
        case["film_title"],
        case["days_overdue"],
        case["fine_rate"],
    )
