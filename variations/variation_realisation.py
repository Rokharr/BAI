import random
import re

class TemplateEngine:

    # метод для підбірки заготовок
    def __init__(self, answers):
        self.templates = answers
        self.default_answers = [answer for (template, answer) in answers if template == ']']

    def cases(self, case, question, answer)

    # обробка питання та підбір заготовленої відповіді
    def get_meaning(self, ask):
    # переводимо в нижній реєстр питання, та створюємо масив
    # з можливими варіантами відповідей, далі перевіряємо всі заготовки
    # виокремлюємо відповіді з ]
    # викидаємо випадковим чином зі створеного масиву нашу відповідь

        ask = ask.lower()
        answers = []
        for (template, answer) in self.templates:
            res = self.cases(template, ask, answer)
            if res is not None:
                answers.append(res)

        if len(answers) > len(self.default_answers):
            answers = [answer for answer in answers if answer not in self.default_answers]
        return answers[random.randint(0, len(answers)-1)]
 


