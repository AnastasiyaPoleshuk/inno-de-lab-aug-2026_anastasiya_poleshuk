-- show which days are most loaded in clinic in 2026

SELECT
  TO_CHAR(dd.full_date, 'Day') day_of_week,
  COUNT(*) AS visit_count,
  dd.is_weekend
FROM 
  fact_visit fv
JOIN 
  dim_date dd ON dd.date_key = fv.date_key
WHERE
  dd.full_date >= DATE '2026-01-01'
  AND dd.full_date < DATE '2027-01-01'
GROUP BY 
  dd.day_of_week,
  dd.is_weekend
ORDER BY 
  visit_count DESC, dd.day_of_week;
