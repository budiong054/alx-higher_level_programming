# 0x0D. SQL - Introduction
---
## Tasks
### 0. List databases
[0-list\_databases.sql]() is a script that list all databases of your MySQL server

### 1. Create a database
[1-create\_databse\_if\_missing.sql]() is a script that creates the database `hbtn_0c_0` in your MySQL server

### 2. Delete a database
[2-remove\_database.sql]() is a script that deletes the database `hbtn_0c_0` in your MySQL server

### 3. List tables
[3-list\_tables.sql]() is a script that list all the tables of a databases in your MySQL server
	* The database name will be passed as argument of `mysql` command

### 4. First table
[4-first\_table.sql]() is a script that creates a table called `first_table` in the current database in your MySQL server
	* `first_table` description: `id` INT and `name` VARCHAR(256)
	* The database name will be passed as an argument of the `mysql` command
	* If the table `first_table` already exists, your script should not fail

### 5. Full description
[5-full\_table.sql]() is a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server
	* The database name will be passed as an argument of the `mysql` command
