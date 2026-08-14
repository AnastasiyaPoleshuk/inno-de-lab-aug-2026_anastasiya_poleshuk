-- task 1. Insert 2 new employees into the Employees table excluding 'IT' department
INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Liz', 'Brown', 'HR', 85000.00),
('Samantha', 'Bartholomew', 'Design', 90000.00);

-- task 2. Select all employees from the Employees table

SELECT * FROM Employees;

-- task 3. Select only the FirstName and LastName of employees from the 'IT' department.

SELECT 
  firstName,
  lastName 
FROM 
  Employees 
WHERE 
  Department = 'IT';

-- task 4. Update "Alice Smith's" salary to 65,000.00.

UPDATE Employees
SET Salary = 65000.00
WHERE FirstName = 'Alice' AND LastName = 'Smith';

-- task 5. Remove the employee 'Eve Davis.'

DELETE FROM Employees
WHERE FirstName = 'Eve' AND LastName = 'Davis';

-- task 6. check changes

SELECT * FROM Employees;