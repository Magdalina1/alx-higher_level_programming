-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

SELECT city, AVG(value) AS AVG_temp FROM `temperature` GROUP BY city ORDER BY AVG_temp DESC; 
