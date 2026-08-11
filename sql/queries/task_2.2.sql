SELECT
  shippings.status,
  customers.first_name,
  customers.last_name
FROM shippings
JOIN customers ON shippings.customer = customers.customer_id