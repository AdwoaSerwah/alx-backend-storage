-- Task: Create stored procedure AddBonus
-- This procedure adds a correction for a student, creating a new project if it doesn't exist.

DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Declare a variable for project ID
    DECLARE project_id INT;

    -- Check if the project exists; if not, insert a new project
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    -- If the project doesn't exist, insert it and get the new project ID
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction into the corrections table
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END$$

DELIMITER ;
