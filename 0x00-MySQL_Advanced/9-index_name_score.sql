-- Task: Create a composite index idx_name_first_score on the first letter of the `name` column and the `score` column.

-- Create an index named `idx_name_first_score` on the first letter of the `name` column and `score`
CREATE INDEX idx_name_first_score ON names (name(1), score);
