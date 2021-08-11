#for patient table:
insert into patient(p_name,gender,age,email,phone_no) values('mahathi','F',20,'mns@gmail.com','9988998899');
insert into patient(p_name,gender,age,email,phone_no) values('abc','M',40,'abc@gmail.com','1111111111'),('ana','F',30,'ana@gmail.com','1111111112'),
('bhavana','F',50,'bvb@gmail.com','2221111111');


#for departments table:
insert into departments values('orthopedics','bones'),('cardiology','heart');
insert into departments values('oncology','cancer'),('general medicine','general');

#for doctor table:
insert into doctor(doc_name,d_gender,age,email,phone_no,department,salary) values('dr.shiva','M',45,'ab@gmail.com','8888888888','cardiology',70000);
insert into doctor(doc_name,d_gender,age,email,phone_no,department,salary) values('dr.anu','F',25,'anu@gmail.com','9988888888','general medicine',50000),
('dr.gagan','M',28,'gg@gmail.com','9999888888','oncology',90000);

#for labTest:
insert into labTest(test_name,test_details,fee) values('blood sugar','sugar content in blood',500);
insert into labTest(test_name,test_details,fee) values('blood pressure','pressure of blood',200),('ECG','heart rate',400),('x-ray','imaging',800);

#for assistTable:
insert into assistTable(lab_id,patient_id,doc_id,issue_date) values(1,1,10,'2020-02-02');
insert into assistTable(lab_id,patient_id,doc_id,issue_date) values(1,2,10,'2020-04-02'),(1,2,10,'2020-04-02');

#for appointment:
insert into Appointment(patient_id,doc_id,app_date) values(1,10,'2020-02-02');
insert into Appointment(patient_id,doc_id,app_date) values(2,11,'2020-10-02');

#for room:
insert into Room(room_type,status) values('general','vaccant');
insert into Room(room_type,status) values('general','vaccant'),('semi special','vaccant'),('special','under renovation');

#for inpatientInfo
insert into inpatientInfo(adm_id,patient_id,room_no,adm_date) values(200,1,1,'2020-02-02');
insert into inpatientInfo(adm_id,patient_id,room_no,adm_date) values(201,2,2,'2020-10-02');

#for Bill:
insert into Bill(billed_for,bill_amt,bill_status,bill_date,patient_id) values('medicines',200,'paid','2020-02-02',1);
insert into Bill(billed_for,bill_amt,bill_status,bill_date,patient_id) values('consultation fee',200,'paid','2020-02-02',1);

#for medicine:
insert into Medicine(m_name,m_date,e_date,company) values('dolo500','2020-01-01','2023-02-02','cipla');
insert into Medicine(m_name,m_date,e_date,company) values('ketorol','2019-01-01','2022-02-02','cipla'),
('cyraD','2020-01-01','2023-04-12','generic'),('moov','2020-01-01','2025-12-02','nameit');

#for Prescription:
insert into Prescription(prs_id,patient_id,doc_id,m_id) values(1,1,10,1);
insert into Prescription(prs_id,patient_id,doc_id,m_id) values(1,1,10,2);

#for users:
insert into users(username,email,passwd) values("user1","abc@hospital.com","abc123");
insert into users(username,email,passwd) values("user2","xyz@hospital.com","abc143");