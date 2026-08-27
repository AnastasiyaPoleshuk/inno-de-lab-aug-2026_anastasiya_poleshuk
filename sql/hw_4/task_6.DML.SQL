-- task 1. check the projects assigned to employee 'Bob Johnson' who has worked more than 150 hours on those projects.

SELECT
    p.ProjectName,
FROM Employees e
JOIN EmployeeProjects ep
    ON e.EmployeeID = ep.EmployeeID
JOIN Projects p
    ON ep.ProjectID = p.ProjectID
WHERE
    e.FirstName = 'Bob'
    AND e.LastName = 'Johnson'
    AND ep.HoursWorked > 150;

-- task 2. update Budget 

UPDATE Projects p
SET 
  Budget = Budget * 1.10
WHERE EXISTS (
    SELECT 1
    FROM EmployeeProjects ep
    JOIN Employees e
        ON ep.EmployeeID = e.EmployeeID
    WHERE 
      ep.ProjectID = p.ProjectID
      AND e.Department = 'Senior IT'
);

SELECT * from Projects

-- task 3. set end date

UPDATE Projects
SET 
  EndDate = StartDate + INTERVAL '1 year'
WHERE 
  EndDate IS NULL;

SELECT
    ProjectID,
    ProjectName,
    StartDate,
    EndDate
FROM Projects;

-- task 4. transaction: add new employee and asin them to project

BEGIN;

WITH new_employee AS (
    INSERT INTO Employees (
        FirstName,
        LastName,
        Department,
        Salary
    )
    VALUES (
        'Anna',
        'Taylor',
        'Senior IT',
        90000.00
    )
    RETURNING EmployeeID
)
INSERT INTO EmployeeProjects (
    EmployeeID,
    ProjectID,
    HoursWorked
)
SELECT
    ne.EmployeeID,
    p.ProjectID,
    80
FROM new_employee ne
JOIN Projects p
    ON p.ProjectName = 'Website Redesign';

COMMIT;