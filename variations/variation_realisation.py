import random
import re

class TemplateEngine:

    def __init__(self, answers):
        self.templates = answers
        self.default_answers = [answer for (template, answer) in answers if template == ']']

    def cases(self, case, question, answer):
        if case.find("]") != -1:
            case = case.replace("]", "")

            if len(case) == 1 and question.find(case) != -1 and answer.find(case) != -1:
                return answer
            

        if case.find("<x>") != -1:
            case = case.replace("<x>", "")

            model = re.compile(rf"((?:{case}\s))(\w+)")
            equivalent = model.search(question)
            if equivalent is None:
                return
            equivalent = equivalent.group(0).replace(case, "").strip()
            return answer.replace("<x>", equivalent)

        if not case:
            return answer

        return answer if question.find(case) != -1 \
            else None

    def get_meaning()


