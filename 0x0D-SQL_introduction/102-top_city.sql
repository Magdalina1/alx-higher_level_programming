-- displays the top 3 of cities temperature during July and August ordered by temperature (descending).

SELECT city, AVG(value) AS AVG_temp FROM temperatures WHERE month IN ('Jully, August') GROUP BY city ORDER BY AVG_temp DESC LIMIT 3;
