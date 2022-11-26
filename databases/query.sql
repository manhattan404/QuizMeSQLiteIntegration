-- CREATE TABLE QUESTIONS (questionID INTEGER NOT NULL PRIMARY KEY, question NOT NULL, answer NOT NULL, subject NOT NULL);

-- INSERT INTO questions (questionID, question, answer, subject)
-- VALUES (3, "What is the powerhouse of the cell?", "Mitochondria", "Biology");

SELECT * FROM questions WHERE subject = "Biology";