use bsc;
CREATE TABLE StudentLeaveOrMeetInfo (
    student_id VARCHAR(15) NOT NULL,
    card_id VARCHAR(50) NOT NULL,
    reason VARCHAR(255) DEFAULT NULL,
    leave_or_meet_date DATETIME DEFAULT NULL,
    expected_return_date DATETIME DEFAULT NULL,
    actual_return_date DATETIME DEFAULT NULL,
    visitor_exit_time DATETIME DEFAULT NULL,
    remark TEXT DEFAULT NULL,
    KEY (student_id)
);
