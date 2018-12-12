#CREATE DATABASE ETL_db;
USE ETL_db;

-- Create Two Tables
DROP TABLE avocado;
CREATE TABLE avocado (
  id INT PRIMARY KEY AUTO_INCREMENT,
  region VARCHAR(50),
  average_price INT,
  total_volume INT);

DROP TABLE census;
CREATE TABLE census (
  id  INT PRIMARY KEY AUTO_INCREMENT,
  region VARCHAR(50),
  city_median_income INT,
  city_median_age INT);
