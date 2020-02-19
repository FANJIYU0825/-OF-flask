CREATE TABLE student (
  student_id INT PRIMARY KEY,
  name VARCHAR(40),
  major VARCHAR(40)
  -- PRIMARY KEY(student_id)
);


DROP TABLE student;
ALTER TABLE student ADD gpa DECIMAL;
ALTER TABLE student DROP COLUMN gpa;
