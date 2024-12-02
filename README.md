# BSC
This project provides a robust framework to manage student leave requests and visitor tracking for colleges and universities. Built with Python for backend business logic and MySQL as the database, the system ensures efficient data handling, validation, and integrity. A key enhancement is the integration of code validation for identifying parents or relatives, ensuring that only authorized individuals are linked to students, enhancing security and operational reliability.

**Core Functionalities:**
1. Student Leave Management:
Students can request leave by providing the purpose, leave date, and expected return date.
The system validates and logs these details securely, associating them with the respective student ID and card ID.
Administrators can monitor, update, or manage these records effortlessly.
2. Visitor Tracking System
Tracks visitor entries and exits, maintaining detailed logs of visitor activities.
Ensures real-time updates of visitor exit times, providing a secure environment for students and staff.

**Key Enhancement: Code Validation for Parents and Relatives**
A standout feature of this system is the integration of code validation for identifying parents and relatives. This mechanism significantly strengthens the security of visitor tracking by ensuring that only authorized individuals can interact with students.

1. Relationship Verification:
During visitor registration, the system requires users to specify their relationship with the student (e.g., parent, sibling, or relative). The provided information is cross-verified against a pre-approved database to prevent unauthorized access.

2. Real-Time Validation:
If a visitor's relationship code does not match the database records, the system prompts for additional validation steps or denies access, ensuring security and accuracy.
