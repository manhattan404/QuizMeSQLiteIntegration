import sqlite3
import mainfile
import mainui


class Quiz:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
