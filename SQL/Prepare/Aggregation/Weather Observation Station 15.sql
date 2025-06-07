/*
Enter your query here.
*/

SELECT 
    ROUND(STATION.LONG_W, 4)
FROM
    STATION
WHERE
    STATION.LAT_N = (SELECT
                        MAX(STATION.LAT_N)
                    FROM
                        STATION
                    WHERE
                        STATION.LAT_N<137.2345);
