/*
Enter your query here.
*/
SELECT 
    MAX(EMPLOYEE.SALARY * EMPLOYEE.MONTHS) AS 'Maximum Total Earnings',
    COUNT(*) AS "COUNT"
FROM
    EMPLOYEE
WHERE
    (EMPLOYEE.SALARY*EMPLOYEE.MONTHS) = 
    (
    SELECT 
        MAX(EMPLOYEE.SALARY*EMPLOYEE.MONTHS)
     FROM 
        EMPLOYEE
        )
