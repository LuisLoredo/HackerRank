/*
Enter your query here.
*/

SELECT 
    ROUND(MIN(STATION.LAT_N), 4)
FROM
    STATION
WHERE
    STATION.LAT_N > 38.7780;
