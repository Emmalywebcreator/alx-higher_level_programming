-- Create the table unique_id if it does not already exist
-- If the table unique_id already exists, your script should not fail

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

