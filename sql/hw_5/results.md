# Vet clinic analytics

## Business process

The model supports veterinary visits. A visit can include several procedures and several product-sale lines. It supports analysis of clinic workload, procedures, retail sales, specialists, pets, and customers.

## Data model

[Open the dimensional model](../../vet_clinic_dwh_snowflake_er_fixed.drawio)

The model is a star schema. Descriptive attributes are kept in dimensions, while transactional events are kept in facts.

### Grain

- `fact_visit`: one row per clinic visit.
- `fact_procedure`: one row per procedure performed during a visit.
- `fact_sales`: one row per product line sold during a visit.

`fact_visit` is the visit header. Both detailed facts reference it through `visit_id`; they are never joined directly at their detailed grain. This prevents the fan-out problem in visits with multiple procedures and sales lines.

### Fact tables

- `fact_visit` stores the visit-level pet, specialist, date, time, and status.
- `fact_procedure` stores the procedure and its price. It references the visit and the procedure, pet, specialist, and date dimensions.
- `fact_sales` stores the product, quantity, and unit price. It also references the specialist, allowing retail revenue and recommendations to be attributed to a specialist.

### Dimension Tables

- `dim_customer` describes the pet owner and supports LTV, household, and contact-based marketing analysis.
- `dim_pet` stores pet attributes and references `dim_customer` through `customer_id`.
- `dim_specialist` includes `speciality_name` directly. A separate low-cardinality speciality dimension would add an unnecessary join.
- `dim_procedure` and `dim_product` describe the respective clinic offerings.
- `dim_date` uses the integer natural key `date_key` in `YYYYMMDD` format, plus the calendar date and derived calendar attributes.

## Analytical questions

### 1. What were the most popular procedures in July 2026?

The query returns procedures ranked by the number of recorded procedures in July 2026.

- [most_popular_procedure.sql](./most_popular_procedure.sql)

### 2. What were the best-selling additional products in July 2026?

The query returns additional products ranked by total units sold in July 2026.

- [most_popular_product.sql](./most_popular_product.sql)

### 3. Which specialists performed the most procedures in July 2026?

Specialists ranked by performed procedures; their speciality is available directly from `dim_specialist`.

- [top_spetialist.sql](./top_spetialist.sql)

### 4. On which days of the week was the clinic busiest in 2026?

The query counts visits from `fact_visit`, rather than procedure rows, so a visit with several procedures is counted once.

- [clinic_load_by_weekday.sql](./clinic_load_by_weekday.sql)
