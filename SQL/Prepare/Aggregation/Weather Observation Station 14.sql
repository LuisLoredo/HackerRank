/*
Enter your query here.
*/
SELECT 
    ROUND(MAX(STATION.LAT_N), 4)
FROM
    STATION
WHERE
    (STATION.LAT_N<137.2345)
