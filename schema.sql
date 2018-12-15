#CREATE DATABASE ETL_db;
USE ETL_db;

-- Create Two Tables

CREATE TABLE avocado (
  id INT PRIMARY KEY AUTO_INCREMENT,
  region VARCHAR(50),
  average_price FLOAT,
  total_volume INT(125));


CREATE TABLE census (
  id  INT PRIMARY KEY AUTO_INCREMENT,
  region VARCHAR(50),
  city_median_income INT,
  city_median_age INT);

SELECT * FROM avocado;

SELECT * FROM census;