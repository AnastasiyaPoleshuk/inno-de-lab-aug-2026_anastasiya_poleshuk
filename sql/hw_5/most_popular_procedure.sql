
-- show the list of procedures by popularity in Jul 2026 

SELECT
  fp.procedure_id,
  dp.name,
  COUNT(*) procedure_count
FROM 
  fact_procedure fp
JOIN 
  dim_procedure dp ON dp.procedure_id = fp.procedure_id
JOIN 
  dim_date dd ON dd.date_id = fp.date_id
WHERE
  EXTRACT(MONTH FROM dd.full_date) = 7 
  AND EXTRACT(YEAR FROM dd.full_date) = 2026
GROUP BY 
  dp.name, dp.procedure_id
ORDER BY 
  procedure_count DESC