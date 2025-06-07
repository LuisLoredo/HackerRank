/*
Enter your query here.
*/

SELECT
    ROUND(STATION.LONG_W, 4)
FROM
    STATION
WHERE
    STATION.LAT_N = (SELECT
                        MIN(STATION.LAT_N)
                    FROM
                        STATION
                    WHERE
                        STATION.LAT_N>38.7780);
