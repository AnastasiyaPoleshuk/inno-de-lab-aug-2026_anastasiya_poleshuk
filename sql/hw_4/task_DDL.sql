-- task 1. create Departments table

CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(50) UNIQUE NOT NULL,
    Location VARCHAR(50)
);

-- task 2. add new Email column to Employees table

ALTER TABLE Employees
ADD COLUMN Email VARCHAR(100);

-- task 3. fill the unique Email column with email for all employees

UPDATE Employees
SET Email = CONCAT(LOWER(FirstName), '.', LOWER(LastName), '@company.com');

-- task 4. add constraint UNIQUE to the Email column

ALTER TABLE Employees
ADD CONSTRAINT unique_email UNIQUE (Email);

-- task 5. rename Location column to OfficeLocation in Departments table

ALTER TABLE Departments
RENAME COLUMN Location TO OfficeLocation;