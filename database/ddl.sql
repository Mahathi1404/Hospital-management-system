CREATE database hmsys
USE hmsys
CREATE TABLE Patient(
patient_id int not null AUTO_INCREMENT,
p_name varchar(255),
gender char(1) not null,
constraint gender check (gender in ('M','F')),
age int,
email varchar(255),
phone_no varchar(10),
PRIMARY KEY (patient_id),
UNIQUE (email)
);



CREATE TABLE Departments(
department varchar(255),
treatment varchar(255),
PRIMARY KEY (department)
);

CREATE TABLE Doctor(
doc_id int NOT NULL AUTO_INCREMENT,
doc_name varchar(255),
d_gender char(1) not null ,
constraint d_gender check (d_gender in ('M','F')),
age int,
email varchar(255),
phone_no varchar(10),
department varchar(255),
salary int,
UNIQUE(email),
PRIMARY KEY (doc_id),
FOREIGN KEY(department) REFERENCES Departments(department)ON UPDATE CASCADE
);
ALTER TABLE Doctor AUTO_INCREMENT=10;


CREATE TABLE labTest(
lab_id int NOT NULL AUTO_INCREMENT,
test_name varchar(255),
test_details varchar(255),
fee int,
PRIMARY KEY (lab_id)
);




CREATE TABLE assistTable(
serial_no int NOT NULL AUTO_INCREMENT,
lab_id int,
patient_id int,
doc_id int,
issue_date date,
PRIMARY KEY (serial_no, lab_id),
FOREIGN KEY(patient_id) REFERENCES Patient(patient_id)ON UPDATE CASCADE,
FOREIGN KEY(doc_id) REFERENCES Doctor(doc_id)ON UPDATE CASCADE,
FOREIGN KEY(lab_id) REFERENCES labTest(lab_id)ON UPDATE CASCADE
);
ALTER TABLE assistTable AUTO_INCREMENT=25;



CREATE TABLE Appointment(
app_id int NOT NULL AUTO_INCREMENT,
patient_id int,
doc_id int,
app_date date,
PRIMARY KEY (app_id,patient_id,doc_id),
FOREIGN KEY(patient_id) REFERENCES Patient(patient_id)ON UPDATE CASCADE,
FOREIGN KEY(doc_id) REFERENCES Doctor(doc_id)ON UPDATE CASCADE
);
ALTER TABLE Appointment AUTO_INCREMENT=100;


CREATE TABLE Room(
room_no int NOT NULL AUTO_INCREMENT,
room_type varchar(255),
status varchar(255),
PRIMARY KEY (room_no)
);



CREATE TABLE inpatientInfo(
adm_id int NOT NULL AUTO_INCREMENT,
patient_id int,
room_no int,
adm_date date,
PRIMARY KEY (adm_id),
FOREIGN KEY(patient_id) REFERENCES Patient(patient_id)ON UPDATE CASCADE,
FOREIGN KEY(room_no) REFERENCES Room(room_no)ON UPDATE CASCADE
);
ALTER TABLE inpatientInfo AUTO_INCREMENT=200;

CREATE TABLE Bill(
bill_no int NOT NULL AUTO_INCREMENT,
billed_for varchar(255),
bill_amt int,
bill_status varchar(255),
bill_date date,
patient_id int,
PRIMARY KEY (bill_no),
FOREIGN KEY(patient_id) REFERENCES Patient(patient_id)ON UPDATE CASCADE
);
ALTER TABLE Bill AUTO_INCREMENT=20;

CREATE TABLE Medicine(
m_id int NOT NULL AUTO_INCREMENT,
m_name varchar(255),
m_date date,
e_date date,
company varchar(255),
PRIMARY KEY (m_id)
);



CREATE TABLE Prescription(
prs_id int NOT NULL AUTO_INCREMENT,
patient_id int,
doc_id int,
m_id int,
PRIMARY KEY (prs_id,m_id),
FOREIGN KEY(patient_id) REFERENCES Patient(patient_id)ON UPDATE CASCADE,
FOREIGN KEY(doc_id) REFERENCES Doctor(doc_id)ON UPDATE CASCADE,
FOREIGN KEY(m_id) REFERENCES Medicine(m_id)ON UPDATE CASCADE
);

ALTER TABLE Prescription AUTO_INCREMENT=200;
create table users(
	username varchar(30),
    email varchar(30),
    passwd varchar(30),
    primary key(email),
    unique(email)
);