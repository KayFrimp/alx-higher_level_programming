-- Create user user_0d_1 giving user all privileges

-- Check if user_0d_1 already exists
SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' LIMIT 1;

-- If user_0d_1 does not exist, create the user with privileges and password
INSERT INTO mysql.user (Host, User, Password) VALUES ('localhost', 'user_0d_1', PASSWORD('user_0d_1_pwd'));

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply changes
FLUSH PRIVILEGES;

-- CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
