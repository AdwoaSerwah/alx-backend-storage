-- 1. In and not out
-- Create a users table with an enumeration for the country attribute
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- id attribute, integer, auto increment, primary key
    email VARCHAR(255) NOT NULL UNIQUE,  -- email attribute, string of max 255 chars, unique and not null
    name VARCHAR(255),  -- name attribute, string of max 255 chars
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'  -- country attribute, ENUM type with default 'US'
);
