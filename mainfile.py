import mainui
import sqlite3
from Quizclass import *

conn = sqlite3.connect('questions.db')

c = conn.cursor()


def addButton():
    with conn:
        quest = mainui.questionEntry.get()
        ans = mainui.answerEntry.get()
        c.execute(
            "INSERT INTO questions VALUES (:question, :answer)", {'question': quest, 'answer': ans})
        print(quest + " and " + ans + " has been added to database")


def displayTable():

    pass
