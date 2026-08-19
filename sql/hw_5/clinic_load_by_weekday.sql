-- show which days are most loaded in clinic in 2026

SELECT
  TO_CHAR(dd.full_date, 'Day') day_of_week,
  COUNT(*) procedure_amount,
  dd.is_weekend
FROM 
  fact_procedure fp
JOIN 
  dim_date dd ON dd.date_id = fp.date_id
WHERE
  EXTRACT(YEAR FROM dd.full_date) = 2026
GROUP BY 
  day_of_week,
  dd.is_weekend     
ORDER BY 
  procedure_amount DESC