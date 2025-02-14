-- Check if the 'budget' column exists
SELECT COUNT(*) INTO @column_exists
FROM information_schema.columns
WHERE table_name = 'projects'
  AND column_name = 'budget'
  AND table_schema = DATABASE();

-- Drop the 'budget' column only if it exists
IF @column_exists > 0 THEN
    ALTER TABLE projects DROP COLUMN budget;
END IF;

-- Add the 'budget' column again
ALTER TABLE projects ADD COLUMN budget DECIMAL(10, 2);