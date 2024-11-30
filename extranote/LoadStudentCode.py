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
    CREATE TABLE IF NOT EXISTS student_code (
        STUDENT_ID VARCHAR(15) PRIMARY KEY,
        student_code VARCHAR(15) UNIQUE NULL,
        student_status INT NULL
    );
    """)
    
    with open(csv_file_path, 'r') as file:
        next(file)  
        for line in file:
            student_id = line.strip().split(',')[0]
            
            cursor.execute("""
            INSERT INTO student_code (STUDENT_ID)
            VALUES (%s);
            """, (student_id,))

    connection.commit()
    cursor.close()
    connection.close()

upload_csv_to_db("bsc_student_id.csv")
