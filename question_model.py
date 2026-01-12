# This class models a single quiz question.
# It exists to bundle question text and its correct answer together,
# making each question a self-contained object.

class Question:
    def __init__(self, q_text, q_answer):
        # The question text shown to the user
        self.text = q_text

        # The correct answer used for validation
        self.answer = q_answer
