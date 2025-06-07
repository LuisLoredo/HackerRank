/*
Enter your query here.
*/

SELECT
    ROUND(SUM(STATION.LAT_N), 2), ROUND(SUM(STATION.LONG_W), 2)
FROM
    STATION;
