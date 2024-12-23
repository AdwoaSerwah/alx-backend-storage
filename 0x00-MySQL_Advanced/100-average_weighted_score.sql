DELIMITER $$

-- Create the stored procedure to compute average weighted score for a user
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weight INT DEFAULT 0;
    DECLARE weighted_sum FLOAT DEFAULT 0;
    DECLARE score FLOAT;
    DECLARE weight INT;
    DECLARE done INT DEFAULT 0;

    -- Declare the cursor first
    DECLARE cur CURSOR FOR
        SELECT c.score, p.weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

    -- Declare the handler for the cursor end
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    
    -- Open the cursor
    OPEN cur;
    
    -- Fetch each row and calculate the weighted sum and total weight
    read_loop: LOOP
        FETCH cur INTO score, weight;
        IF done THEN
            LEAVE read_loop;
        END IF;
        
        SET weighted_sum = weighted_sum + (score * weight);
        SET total_weight = total_weight + weight;
    END LOOP;
    
    -- Close the cursor
    CLOSE cur;
    
    -- Calculate and update the average weighted score for the user
    IF total_weight > 0 THEN
        UPDATE users
        SET average_score = weighted_sum / total_weight
        WHERE id = user_id;
    ELSE
        UPDATE users
        SET average_score = 0
        WHERE id = user_id;
    END IF;
END$$

DELIMITER ;
