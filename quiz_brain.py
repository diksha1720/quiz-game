class Quiz:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.points = 0

    def next_question(self):
        ques = self.questions[self.question_number]
        self.question_number += 1
        return ques.text

    def has_questions(self):
        if self.question_number >= len(self.questions):
            return False
        return True

    def check_answer(self):
        return self.questions[self.question_number-1].ans

    def get_score(self):
        self.points +=1
        return self.points





