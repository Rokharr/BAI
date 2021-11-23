import random
import re

class TemplateEngine:

    def __init__(self, answers):
        self.templates = answers
        self.default_answers = [answer for (template, answer) in answers if template == ']']

    def cases(self, case, question, answer):
        # if template contains '*' operator
        if case.find("]") != -1:
            case = case.replace("]", "")

            # if template contains only one char along with '*', and both answer and question has this char
            if len(case) == 1 and question.find(case) != -1 and answer.find(case) != -1:
                return answer

    def get_meaning()


