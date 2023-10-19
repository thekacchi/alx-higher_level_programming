-- Create the unique_id table if it doen't exist
CREATE TABLE IF NOT EXISTS unique_id (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256)
) ENGINE=InnoDB;

-- Set the default value if the id column to 1
ALTER TABLE unique_id MODIFY id INT NOT
NULL DEFAULT 1;

-- Add a unique constrait to ensure id value are unique
ALRER TABLE unique_id ADD CONSTRAINT
unique_id_id_unique UNIQUE (id);
