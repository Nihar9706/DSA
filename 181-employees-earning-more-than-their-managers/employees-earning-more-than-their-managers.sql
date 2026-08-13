/* Write your T-SQL query statement below */

SELECT employee.name AS Employee

FROM Employee employee

-- Match each employee with their manager
JOIN Employee manager
    ON employee.managerId = manager.id

-- Keep only employees earning more than their manager
WHERE employee.salary > manager.salary;