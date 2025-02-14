USE companydb;

CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT PRIMARY KEY,
    project_name VARCHAR(255) NOT NULL,
    start_date DATE,
    end_date DATE
);

-- Drop the 'budget' column if it exists
ALTER TABLE projects DROP COLUMN IF EXISTS budget;

-- Add the 'budget' column again
ALTER TABLE projects ADD COLUMN budget DECIMAL(10, 2);