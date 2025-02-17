# Prog8850_DB-Assignment2
Automating Database Schema Changes and CI/CD for Database Deployment

This project shows how to use GitHub Actions and Azure MySQL to automate database schema updates and construct a CI/CD pipeline for database deployment.
## Project Structure
├── schema_changes.sql       # SQL script to modify the database schema
├── add_departments.sql      # SQL script to add the 'departments' table
├── execute_sql.py           # Python script to automate SQL execution
├── .github/
│   ├── workflows/
│   │   ├── ci_cd_pipeline.yml  # GitHub Actions workflow file
├── requirements
└── README.md                # Documentation

## Steps to Run Locally
1. Setup Azure MySQL Database
        1. Log in to Azure Portal.
        2. Create a MySQL Flexible Server instance.
        3. Set the Server Name, Admin Username, and Password.
        4. Configure Firewall Rules to allow access from your local machine.
        5. Create a new database named companydb.

2. Connect to Azure MySQL from VS Code
    Run the following command in PowerShell:  mysql -u <MYSQL_USER> -p -h <MYSQL_HOST>
    Enter your password when prompted.

3. Run SQL Script Using Python
    Execute the schema_changes.sql script using: python execute_sql.py
    This script connects to the database and applies schema changes.

## CI/CD Pipeline Setup
1. Configure GitHub Secrets
        In the repository:
    Go to Settings > Secrets and variables > Actions.
    Add the following secrets:
        DB_HOST - Azure MySQL hostname
        DB_USER - MYSQL Admindatabase username
        DB_PASSWORD - MySQL database password
        DB_NAME - database name (companydb)

2. GitHub Actions Workflow
    (.github/workflows/ci_cd_pipeline.yml)
    ci_cd_ workflow automates database schema changes on a push to main

3. Testing the CI/CD Pipeline
   1. Modify schema_changes.sql to update the database schema.
   2. Commit and push the changes
        git status
        git add .
        git commit -m "Updated schema_changes.sql"
        git push origin main  
    3. Monitor GitHub Actions in the Actions tab to check deployment status.

4. Troubleshooting
    Issue: SQL Script Execution Fails
    1. Ensure the database name is correctly specified.
    2. Verify Azure firewall rules allow connections.
    3. Confirm MySQL user permissions.

    Issue: Duplicate Column Name Error

    If ALTER TABLE fails due to an existing column, drop it manually:
    ALTER TABLE projects DROP COLUMN IF EXISTS budget;

5. Conclusion
    This project automates MySQL database schema changes and integrates a CI/CD pipeline for seamless deployments using GitHub Actions and Azure 
