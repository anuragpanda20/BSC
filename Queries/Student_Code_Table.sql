use bsc;
CREATE TABLE student_code (
    STUDENT_ID VARCHAR(15) NOT NULL,
    student_code VARCHAR(15) UNIQUE DEFAULT NULL,
    student_status INT DEFAULT NULL,
    PRIMARY KEY (STUDENT_ID)
);