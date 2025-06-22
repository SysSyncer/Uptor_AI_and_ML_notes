### Types of Database
- **Type 1** Structured Database 
  - Oracle SQL
  - PostgreSQL
  - MySQL
- **Type 2** Unstructured Database
  - MongoDB
  - Redis

### MySQL
- In order to communicate with these databases, we need a specific language medium. This language is what we commonly call as **SQL** (Structured Query Language).
  - **MySQL** (Server) runs as a service at ```localhost:3306``` or ```127.0.0.1:3306``` (Default).
  - **Workbench** (Client)

### To communicate with mysql
- **Step 1:** Open the mysql workbench.
- **Step 2:** Connect to the database instances.
- **Step 3:** Connect to the database.
- **Step 4:** Execute a command and get an output.
  - **Step 4.1** Types of commands
    - **Step 4.1.1** DDL (Data Definition Language) - *interview*
    - **Step 4.1.2** DML (Data Manipulation Language) - *interview*
    - **Step 4.1.3** DCL (Data Control Language)
    - **Step 4.1.4** TCL (Transaction Control Language)
    - **Step 4.1.5** DQL (Data Query Language)
> **DML** - The command the revolves around data and data related activity.\
> **DDL** - The command the does not revolve around data and data related activity.

### Methods for running MySQL
1. Through the workbench tool.
2. Through command line interface.
3. Through any programming language. 
   1. Most commonly used programming language in our case is python.
   2. To execute MySQL on python, we need to install library.
      - ```pip install mysql-connector-python```
      - Even though we installed in the name of ```mysql-connector-python```, we will be importing it as ```import mysql.connector```