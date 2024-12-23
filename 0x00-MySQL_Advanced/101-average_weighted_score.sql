DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT 0;
    DECLARE user_id INT;
    DECLARE weighted_sum FLOAT;
    DECLARE total_weight INT;
    DECLARE cur CURSOR FOR
        SELECT DISTINCT c.user_id
        FROM corrections c;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    -- Open the cursor
    OPEN cur;

    -- Loop through all users in corrections table
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate weighted sum and total weight for the user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO weighted_sum, total_weight
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Avoid division by zero (if total_weight is zero)
        IF total_weight > 0 THEN
            -- Update the average score for the user
            UPDATE users
            SET average_score = weighted_sum / total_weight
            WHERE id = user_id;
        ELSE
            -- If no projects or weights, set average_score to 0
            UPDATE users
            SET average_score = 0
            WHERE id = user_id;
        END IF;
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END$$

DELIMITER ;
