import sqlite3
import main
import mainui


class Quiz:

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
