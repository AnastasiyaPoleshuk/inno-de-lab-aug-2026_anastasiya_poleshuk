MAX_RENTAL_BATCH_LIMIT = 150.0

test_values = [
  { 'id': 1, 'name': "Academy Dinosaur", 'quantity': 30, 'rental_rate': 2.99},
  { 'id': 2, 'name': "Affair Prejudice", 'quantity': 40, 'rental_rate': 4.99, 'discount': 0.10},
  { 'id': 3, 'name': "Agent Truman", 'quantity': 10, 'rental_rate': 1.99},
  { 'id': 4, 'name': "African Egg", 'quantity': 50, 'rental_rate': 3.50, 'discount': 0.20},
]


def calculate_rental_batch(quantity: int, rental_rate: float, discount = 0.0) -> tuple[float, bool]:
  """Calculate rental batch total and check if it exceeds the limit
  
    Args:
      * quantity - number of disks in a batch
      * rental_rate - cost of one disk
      * discount - discount (if any)
    
    Returns:
      * final_sum - sum of all batch with discount (if any)
      * is_limit_exceeded - true if final_sum is more than MAX_RENTAL_BATCH_LIMIT
  """
  final_sum = round(quantity * rental_rate * (1 - discount), 2)
  return (final_sum, final_sum > MAX_RENTAL_BATCH_LIMIT)


print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

for item in test_values:
  result = ()
  if "discount" in item:
    result = calculate_rental_batch(item["quantity"], item["rental_rate"], discount = item["discount"])
  else:
    result = calculate_rental_batch(item["quantity"], item["rental_rate"])

  print(f"Партия {item["id"]} ({item["name"]}): Сумма {result[0]}$. Превышение лимита: {result[1]}")