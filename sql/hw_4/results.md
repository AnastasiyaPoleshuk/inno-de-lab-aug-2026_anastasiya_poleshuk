## RESULTS — Homework 4

### task_DDL

- [SQL script](./task_DDL.sql)
- Result: created the `Departments` table; added the `Email` column to `Employees`, populated it, and applied a unique constraint. The `Location` column was renamed to `OfficeLocation`.

![DDL result 1](../../screenshots/sql_results/task_DDL_1.png)

![DDL result 2](../../screenshots/sql_results/task_DDL_2.png)

### task_DML

- [SQL script](./task_DML.sql)
- Result: added Liz Brown and Samantha Bartholomew; selected all employees and the employees from the `IT` department; updated Alice Smith's salary to `65000.00`; deleted Eve Davis; and checked the final contents of `Employees`.

![DML result](../../screenshots/sql_results/task_DML.png)

### task_DCL

- [SQL script](./task_DCL.sql)
- Result: created the `hr_user` role and granted `SELECT` access to `Employees`. `INSERT` was initially denied; after granting `INSERT`, `UPDATE`, and `USAGE` on `employees_employeeid_seq`, inserting a new employee succeeded.

![DCL test 1](../../screenshots/sql_results/task_DCL_test_1.png)

![DCL test 2](../../screenshots/sql_results/task_DCL_test_2.png)

![DCL test 3](../../screenshots/sql_results/task_DCL_test_3.png)

### task_DML_DCL

- [SQL script](./task_DML_DCL.sql)
- Result: increased salaries in the `HR` department by 10%; changed the department to `Senior IT` for employees with a salary above `70000.00`; removed employees without project assignments; and, in a transaction, created the `Data Warehouse` project and assigned it to employees with IDs `3` and `4`.

![DML/DCL transaction result](../../screenshots/sql_results/task_DML_DCL_4.png)

### task_6.DML

- [SQL script](./task_6.DML.SQL)
- Result: selected Bob Johnson's projects with more than 150 hours worked; increased the budget by 10% for projects staffed by the `Senior IT` department; set a one-year end date for projects without one; and, in a transaction, created Anna Taylor and assigned her to the `Website Redesign` project.

![Task 6 — project selection](../../screenshots/sql_results/task_6.DML_1.png)

![Task 6 — project budget update](../../screenshots/sql_results/task_6.DML_2.png)

### task_func

- [SQL script](./task_func.sql)
- Result: created the `CalculateAnnualBonus` function, which returns 10% of an employee's salary; displayed employee bonuses; created `IT_Department_View` for the `Senior IT` department; and displayed the view.

![Function result](../../screenshots/sql_results/task_func_1.png)

![View result](../../screenshots/sql_results/task_func_2.png)
