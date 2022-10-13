import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',password='manager')
mycursor=conn.cursor()
conn.autocommit = True
mycursor.execute("create database employees")
mycursor.execute("use employees")
mycursor.execute("create table log_id(user_id varchar(20) ,password  varchar(100) primary key)")
mycursor.execute("create table office (em_no bigint,em_name varchar(255),em_dept varchar(255),em_salary int,em_age int)")

mycursor.execute("create table em_performance (em_no bigint,em_name varchar(255),em_dept varchar(255),em_performance varchar(255),em_work varchar(255))")
