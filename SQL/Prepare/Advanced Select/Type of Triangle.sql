
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/
SELECT CASE WHEN (A+B<=C OR A+C<=B OR B+C<=A) THEN 'Not A Triangle' WHEN (A=B AND B=C) THEN 'Equilateral' WHEN (A=B OR A=C OR B=C) THEN 'Isosceles' ELSE 'Scalene' END TRIANGLENAME FROM TRIANGLES;
