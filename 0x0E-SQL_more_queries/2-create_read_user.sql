-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create 'user_0d_1' if it doesn't exist
CREATE USER IF NOT EXISTS
'user_0d_2'@'localhost' IDENTIFIED BY
'user_0d_2_pwd';

-- Grant USAGE privileg to 'user_0d_1' on all databases
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';

GRANT SELECT ON 'hbtn_0d_2.' TO 'user_0d_2'@'localhost';

-- Flush provileges to apply changes
FLUSH PRIVILEGES
