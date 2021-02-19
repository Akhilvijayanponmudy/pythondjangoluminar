# show databases;
# create database python;
# use python;
# create table student(rol int,name varchar(200),cource varchar(150),total int);
# show tables
# desc student;
# insert into students(rol,name,cource,total)value(100,'akhil','mca',300);
# select * from students;
# update students set total=325 where rol=100;
# select * from students where rol=100;
# delete from students where rol=103;
# select count(*) from employee;
# select count(*),desig from employee group by desig;
# select desig,count(*) from employee group by desig;
# select name,max(salary) from employee where desig='developer';
# select max(salary) from employee;
# select min(salary) from employee;
# select min(salary),desig from employee group by (desig);
# --join querry>>>> select employee,name,location.l_name from employee,location where employee,eid=location.eid and location,l_name='mumbai';
# show tables;
# select name from emp where salary=(select max(salary)from emp);
# select max(salary) from emp where salary <> (select max(salary) from emp);
# select dept from emp group by dept having count(*) <2;
# alter table emp drop coloumn dept;





