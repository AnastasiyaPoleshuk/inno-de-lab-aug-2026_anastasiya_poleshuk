SELECT
  country, COUNT(customer_id) AS count
FROM customers
GROUP BY country