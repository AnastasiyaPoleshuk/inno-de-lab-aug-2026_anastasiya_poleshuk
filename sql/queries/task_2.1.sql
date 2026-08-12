SELECT
  c.first_name, 
  c.last_name,
  o.item,
  o.amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id