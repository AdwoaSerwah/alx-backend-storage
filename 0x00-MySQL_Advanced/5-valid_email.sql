DELIMITER $$

CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF OLD.email != NEW.email THEN
        -- Reset valid_email to 0 if the email has changed
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;
