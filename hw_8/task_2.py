import time
from typing import Any, Callable

PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8

standard_revenue_data = [
    {"category": "Action", "total_sales": 4311.85},
    {"category": "Animation", "total_sales": 4656.30},
    {"category": "Children", "total_sales": 3655.55},
]

equal_revenue_data = [
    {"category": "Classics", "total_sales": 1200.10},
    {"category": "Comedy", "total_sales": 4000.00},
    {"category": "Documentary", "total_sales": 4000.00},
]

single_category_data = [
    {"category": "Drama", "total_sales": 500.00},
]

test_data = [
    {"id": 1, 'data': standard_revenue_data},
    {"id": 2, 'data': equal_revenue_data},
    {"id": 3, 'data': single_category_data},
]

def performance_logger(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        result = func(*args, **kwargs)

        execution_time = time.perf_counter() - start_time

        print(f"{PERFORMANCE_LOG_PREFIX} Функция '{func.__name__}' выполнена за {execution_time:.{TIME_DECIMALS}f} сек.")

        return result

    return wrapper

@performance_logger
def get_sorted_report(data:  list[dict[str, str | float]]) ->  list[dict[str, str | float]]:
    """Sort genre revenue records by total sales in descending order

    Args:
        data - list of dictionaries containing ``category`` and ``total_sales`` keys

    Returns:
        new list of the provided revenue records sorted by ``total_sales``
    """
    return sorted(data, key=lambda x: x['total_sales'], reverse=True)


print("=== ТЕСТИРОВАНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ===")

for item in test_data:
    print(f"--- ТЕСТ {item["id"]} ---")
    sorted_report = get_sorted_report(item["data"])
    for i in range(len(sorted_report)):
      print(f"{i + 1}. {sorted_report[i]['category']}: {sorted_report[i]['total_sales']}")
