import ui
import sqlite3

# ----------------------------------------------------------------------------------------


def addButton():
    print("Button is pressed")

    user_question = ui.questionEntry.get()
    print(user_question)

    user_answer = ui.answerEntry.get()
    print(user_answer)

# ----------------------------------------------------------------------------------------
# Connection to database


conn = sqlite3.connect('questions.db')

c = conn.cursor()

c.execute(
    """INSERT INTO questions (question, answer) VALUES ('another test','its working')""")

conn.commit()

conn.close()
