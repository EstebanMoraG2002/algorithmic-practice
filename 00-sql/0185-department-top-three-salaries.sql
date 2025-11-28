-- Write your PostgreSQL query statement below
SELECT 
    d.name as Department,
    t.name as Employee,
    t.salary as Salary
FROM (
    SELECT 
        name,
        departmentId,
        salary,
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
) AS t
JOIN Department d ON t.departmentId= d.id
WHERE rnk <= 3;
