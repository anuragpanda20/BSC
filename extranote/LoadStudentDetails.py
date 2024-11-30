import mysql.connector

def upload_csv_to_db(csv_file_path):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  
        password='password',  
        database='bsc'
    )
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student_details (
        SI_NO INT AUTO_INCREMENT PRIMARY KEY,
        student_id VARCHAR(15) UNIQUE,
        STUDENT_NAME VARCHAR(255) NOT NULL,
        HOSTEL_ID VARCHAR(15),
        FATHER_NAME VARCHAR(255),
        MOTHER_NAME VARCHAR(255),
        PRIMARY_GUARDIAN VARCHAR(255),
        PRIMARY_NO VARCHAR(15),
        SECONDARY_NO VARCHAR(15),
        student_status INT,
        EMAIL VARCHAR(255) UNIQUE
    );
    """)

    with open(csv_file_path, 'r') as file:
        next(file) 
        for line in file:
            student_id, student_name, father_name, mother_name, primary_no, secondary_no = line.strip().split(',')
            cursor.execute("""
            INSERT INTO student_details (student_id, student_name, father_name, mother_name, primary_no, secondary_no)
            VALUES (%s, %s, %s, %s, %s, %s);
            """, (student_id, student_name, father_name, mother_name, primary_no, secondary_no))

    connection.commit()
    cursor.close()
    connection.close()

upload_csv_to_db("bsc_student_data.csv")
