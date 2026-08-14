-- task 1. function for calculating bonus

CREATE OR REPLACE FUNCTION CalculateAnnualBonus(
    employee_id INTEGER,
    Salary DECIMAL(10, 2)
)
RETURNS DECIMAL(10, 2)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN Salary * 0.10;
END;
$$;

-- task 2. check the function with employees table

SELECT 
    EmployeeID, 
    FirstName, 
    LastName, 
    Salary, 
    CalculateAnnualBonus(EmployeeID, Salary) AS AnnualBonus
FROM 
    Employees;

-- task 3. create a view for the IT department

CREATE VIEW IT_Department_View AS
SELECT 
    EmployeeID, 
    FirstName, 
    LastName, 
    Salary
FROM 
    Employees
WHERE 
    Department = 'Senior IT'; -- after all manipulations 'IT' department was renamed to 'Senior IT' for all employees with a salary greater than 70,000.00

-- task 4. check the view

SELECT * FROM IT_Department_View;