-- Create 'user_0d_1' if it doesn't exist
CREATE USER IF NOT EXISTS
'user_0d_2'@'localhost' IDENTIFIED BY
'user_0d_2_pwd';

-- Grant all privileges to 'user_0d_1'
GRANT ALL PRIVILEGES ON *.* TO
'user_0d_2'@'localhost' WITH GRANT OPTION;

-- Flush provileges to apply changes
FLUSH PRIVILEGES
