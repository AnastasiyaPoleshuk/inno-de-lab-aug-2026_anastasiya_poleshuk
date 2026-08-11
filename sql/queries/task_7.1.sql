SELECT
  CONCAT(customers.first_name, ' ', customers.last_name) AS full_name,
  customers.country,
  COUNT(orders.order_id) AS total_orders,
  SUM(orders.amount) AS total_amount
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
WHERE (
  SELECT COUNT(status = 'Delivered')
  FROM shippings
  WHERE orders.customer_id = customers.customer_id
) >= 1
GROUP BY customers.customer_id
HAVING COUNT(orders.customer_id) >= 2
