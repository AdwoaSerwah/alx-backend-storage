-- Task: Create stored procedure ComputeAverageScoreForUser
-- This procedure computes the average score for a student and stores it in the users table.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    -- Declare a variable to store the computed average score
    DECLARE avg_score FLOAT;

    -- Calculate the average score from the corrections table for the given user_id
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = user_id;

    -- Update the user's average_score with the calculated average
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END$$

DELIMITER ;
