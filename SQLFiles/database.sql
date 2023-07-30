#to create database
CREATE DATABASE test;

#drop database
DROP DATABASE test;

#to create table
CREATE TABLE COMPANY1(
     ID  INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE  INT NOT NULL,
     ADDRESS CHAR(50),
     SALARY REAL
);

CREATE TABLE DEPARTMENT(
  ID INT PRIMARY KEY NOT NULL,
  DEPT CHAR(50) NOT NULL,
  EMP_ID  INT NOT NULL
);

SELECT * FROM company;

#Insert
INSERT INTO company(ID,NAME,AGE,ADDRESS,SALARY)
VALUES
(2,"Zar",25,"Yangon",100000),
(3,"Thwe",25,"Yangon",100000),
(4,"Tech",25,"Yangon",100000),
(5,"Neural",25,"Yangon",100000),
(6,"IT",25,"Yangon",100000)
;

#id,name,salary from company
SELECT ID,NAME,SALARY FROM company;

#update
UPDATE company 
SET ADDRESS = "Mandalay" 
WHERE id=4;

#update salary of the employee's id=3 to 25000
UPDATE company SET SALARY = 25000 WHERE id = 3;

#DELETE
DELETE FROM company 
WHERE id = 3;

#Operators
#Arithmetic Operators ----  + , - , * , /,%
#Compairson Operators --- =, Not equal to --> <> or !- ,< ,> <= , >=
#Logical Operators --- AND,OR,NOT

#AND Operator
SELECT * FROM company WHERE age>=26 AND salary > 100000;

#OR operator
SELECT * FROM company WHERE age>25 OR salary > 100000;

#COUNT -- total number of rows
SELECT COUNT(*) FROM company;

SELECT COUNT(*) FROM company WHERE age = 25;

#SUM  --- to calculate sum of values in a specified column 
SELECT SUM(salary) FROM company;

#LIKE --> to match a specified pattern of charcters in a string
#(%) and (_)

-- SELECT * FROM table_name 
-- WHERE column LIKE 'XXXX%';

-- SELECT * FROM table_name 
-- WHERE column LIKE '%XXXX%';

-- SELECT * FROM table_name 
-- WHERE column LIKE 'XXXX_';
-- SELECT * FROM table_name 
-- WHERE column LIKE '_XXXX_';

-- SELECT * FROM table_name 
-- WHERE column LIKE '_XXXX';

#LIMIT
SELECT * FROM company LIMIT 3;

#ORDER BY  --> sort in ascending or descending order
SELECT * FROM company ORDER BY SALARY DESC;
SELECT * FROM company ORDER BY SALARY ASC;

#GROUP BY --- is used to group rows based on one or more columns
SELECT SUM(salary) FROM company;

#find out total amount of salary of each name;
SELECT NAME,SUM(salary) FROM company GROUP BY NAME;



