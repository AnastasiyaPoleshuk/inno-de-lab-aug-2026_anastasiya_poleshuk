-- task 1. Create a new role named “hr_user” with a password

CREATE ROLE hr_user 
WITH LOGIN PASSWORD 'hr_user_password';

-- task 2. Grant  hr_user role SELECT on Employees table

GRANT SELECT ON TABLE Employees TO hr_user;

-- check 1

SELECT * FROM Employees; --success

-- check 2

INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('NEW', 'USER', 'HR', 0.00); --fail

-- task 3. Grant hr_user role INSERT and UPDATE on Employees table

GRANT INSERT, UPDATE ON TABLE Employees TO hr_user;

GRANT USAGE ON SEQUENCE employees_employeeid_seq TO hr_user; -- had to add permissions for employees_employeeid_seq because the EmployeeID is a SERIAL column and uses a sequence to generate unique IDs.

-- check 3

INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('NEW', 'USER', 'HR', 0.00); --success 