-- Use the hbtn.. database
USE hbtn_0d_usa;

SELECT cities.id, cities.state_id
FROM cities
WHERE cities.state_id = (SELECT id FTOM states WHERE name = 'California')
ORDER BY cities.id;
