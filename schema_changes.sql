Use companydb;

-- Create the projects table if it doesn't exist
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Check if the 'budget' column already exists before adding it
SET @column_exists = (SELECT COUNT(*) 
                      FROM information_schema.columns 
                      WHERE table_name = 'projects' 
                      AND column_name = 'budget');

-- Add the 'budget' column only if it doesn't exist
IF @column_exists = 0 THEN
    ALTER TABLE projects ADD COLUMN budget DECIMAL(10, 2);
END IF;