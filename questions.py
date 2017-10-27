# This is the object class which holds the questions, answers and choices
# for the trivia game.


class Questions:

    def __init__(self, question, choices, answer):
        # method initializes data attributes
        self.question = question
        self.choices = choices
        self.answer = answer

# Mutators, pass arguments
    def set_question(self, question):
        self.question = question

    def set_choices(self, choices):
        self.choices = choices

    def set_answer(self, answer):
        self.answer = answer


# Accessors, returns variable
    def get_question(self):
        return self.question

    def get_choices(self):
        return self.choices

    def get_answer(self):
        return self.answer
