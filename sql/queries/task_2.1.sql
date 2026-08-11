SELECT
  customers.first_name, 
  customers.last_name,
  orders.item,
  orders.amount
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id