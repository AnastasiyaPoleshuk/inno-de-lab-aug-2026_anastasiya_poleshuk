SELECT
  item,
  COUNT(order_id) AS count,
  ROUND(AVG(amount), 2) AS avg_amount
FROM orders
GROUP BY item
