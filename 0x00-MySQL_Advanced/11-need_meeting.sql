-- Create a view 'need_meeting' that lists all students who need a meeting.
-- They must have a score strictly under 80, and either have no last meeting
-- or their last meeting was more than a month ago.

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
