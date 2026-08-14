-- task 1. Update the salary of 'HR' department by 10%.

UPDATE 
  Employees
SET 
  Salary = Salary * 1.10
WHERE 
  Department = 'HR'

-- task 2. Update the department of employees with a salary greater than 70,000.00 to 'Senior IT'.

UPDATE 
  Employees
SET 
  Department = 'Senior IT'
WHERE 
  Salary > 70000.00

-- task 3. Delete all employees who are not assigned to any project.

DELETE FROM Employees e
WHERE NOT EXISTS (
  SELECT 1
  FROM EmployeeProjects ep
  WHERE ep.EmployeeID = e.EmployeeID
);

-- task 4. transaction: Insert a new project into Projects table and assign it to two employees.

BEGIN;

WITH new_project AS (
    INSERT INTO Projects (ProjectName, Budget, StartDate, EndDate)
    VALUES ('Data Warehouse', 200000.00, '2026-08-01', '2026-12-31')
    RETURNING ProjectID
)

INSERT INTO EmployeeProjects (EmployeeID, ProjectID, HoursWorked)
SELECT 3, ProjectID, 80
FROM new_project

UNION ALL

SELECT 4, ProjectID, 100
FROM new_project;

SELECT * FROM EmployeeProjects;

COMMIT;