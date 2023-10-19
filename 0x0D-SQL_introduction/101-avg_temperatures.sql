-- Displays the average temperature in Farenheit, in descending order
SELECT city, AVG(value) AS acg_temp
FROM temperatures
GROUP BY city
ORDER BY acg_temp DESC;
