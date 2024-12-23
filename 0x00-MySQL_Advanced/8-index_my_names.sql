-- Task: Create an index on the first letter of the `name` column in the `names` table.

-- Create an index named `idx_name_first` on the first letter of the `name` column
CREATE INDEX idx_name_first ON names (name(1));
