-- Task: Create stored procedure ComputeAverageScoreForUser
-- Computes the average score for a student and stores it in the users table.

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN input_user_id INT)
BEGIN
    -- Declare a variable to store the computed average score
    DECLARE avg_score FLOAT;

    -- Calculate the average score for the given user
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = input_user_id;

    -- Update the user's average_score with the calculated average
    UPDATE users
    SET average_score = avg_score
    WHERE id = input_user_id;
END$$

DELIMITER ;
