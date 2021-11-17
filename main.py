from variations import TemplateEngine

if __name__ == '__main__':
    with open('answer_sheet.txt', 'r') as cases_2_answer:
        answer = []
        for case in cases_2_answer.readlines():
            answer.append(tuple(case.split('_')))
        engine = TemplateEngine(answer)
        while True:
            text = input()
            print(engine.get_meaning(text))