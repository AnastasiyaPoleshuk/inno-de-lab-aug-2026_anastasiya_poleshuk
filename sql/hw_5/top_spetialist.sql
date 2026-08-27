-- show top of specialists in Jul 2026

SELECT
  ds.specialist_id,
  CONCAT(ds.first_name, ' ', ds.last_name) full_name,
  ds.speciality_name,
  COUNT(*) procedure_count
FROM 
  fact_procedure fp
JOIN 
  dim_specialist ds ON ds.specialist_id = fp.specialist_id
JOIN 
  dim_date dd ON dd.date_key = fp.date_key
WHERE
  EXTRACT(MONTH FROM dd.full_date) = 7 
  AND EXTRACT(YEAR FROM dd.full_date) = 2026
GROUP BY 
  ds.specialist_id,
  ds.first_name,
  ds.last_name, 
  ds.speciality_name
ORDER BY 
  procedure_count DESC, full_name;
