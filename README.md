# Setting Environment

1. Run server: ```python2.7 -m CGIHTTPServer 8000```
2. Install postgreAQL: ```sudo apt-get install postgresql postgresql-contrib```
  - Run postgreAQL: ```sudo -i -u postgres```
  - Please reset password to "postgres" use command: ```\password postgres```
  Create table: 
  ```
  CREATE TABLE account (
    user_id serial PRIMARY KEY,
    user_account varchar (50) NOT NULL,
    user_password varchar (100) NOT NULL,
    first_name varchar(25) NOT NULL,
    last_name varchar(25) NOT NULL
  );
  ```
  ```
  CREATE TABLE signin (
      id serial PRIMARY KEY,
      account varchar (50) NOT NULL,
      password varchar (100) NOT NULL,
      ip varchar (50) NOT NULL
  );
  ```
3. Python need to import psycopg2 use command: ```sudo apt-get install python-psycopg2```
