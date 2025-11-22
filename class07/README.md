# RDS MySQL Database Project

This project involved creating an RDS database in MySQL, managing tables and data through SQL scripts, and practicing backup/restore operations.

## Project Structure

### VPC Creation

- The VPC for this project was created using the script: `class07/vpc_script.sh`

### Database Setup

- MySQL RDS database was created through AWS Management Console
- Database was configured to use MySQL engine
- Backup/snapshot functionality was utilized for data protection

### SQL Scripts Execution

#### Initial Database Setup

- `class07/rds_database_create_table.sql` - Created the database, `sales` table, and inserted initial data

#### Data Management

- `class07/add_more_data.sql` - Inserted additional records into the `sales` table
- `class07/drop_sales_table.sql` - Dropped the `sales` table to simulate data loss scenario

#### Backup Operations

- `class07/read_backup_database.sql` - Used to read records from the backed up database after restoration from snapshot

### Key Operations

1. Created RDS MySQL instance within custom VPC
2. Established `sales` table
3. Performed data insertion operations
4. Tested backup/restore workflow by:
   - Dropping the `sales` table
   - Restoring from snapshot backup
   - Verifying data integrity

### Table Information

- Primary table name: `sales`

Class details in the following link https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Cloud%20para%20dados/Aula_07
