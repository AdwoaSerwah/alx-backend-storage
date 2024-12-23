-- 0. We are all unique!
-- Create a users table with unique email and necessary constraints
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- id attribute, integer, auto increment, primary key
    email VARCHAR(255) NOT NULL UNIQUE,  -- email attribute, string of max 255 chars, unique and not null
    name VARCHAR(255)  -- name attribute, string of max 255 chars
);
