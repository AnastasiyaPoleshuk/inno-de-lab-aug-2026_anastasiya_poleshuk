
-- show the list of products by popularity in Jul 2026 

SELECT
  dp.name,
  SUM(fs.quantity) sum_quantity
FROM 
  fact_sales fs
JOIN 
  dim_product dp ON dp.product_id = fs.product_id
JOIN 
  dim_date dd ON dd.date_id = fs.date_id
WHERE
  EXTRACT(MONTH FROM dd.full_date) = 7 
  AND EXTRACT(YEAR FROM dd.full_date) = 2026
GROUP BY 
  dp.name, dp.product_id
ORDER BY 
  sum_quantity DESC