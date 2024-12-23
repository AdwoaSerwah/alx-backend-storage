-- 4. Buy buy buy
-- Create a trigger that decreases the quantity of an item after adding a new order

DELIMITER $$  -- Change delimiter to handle multi-statement triggers

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the quantity in the items table by subtracting the number of items ordered
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;  -- Reset delimiter to default
