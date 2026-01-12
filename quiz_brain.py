# This class manages the quiz logic.
# It controls:
# - Which question is being asked
# - User input
# - Answer checking
# - Score tracking

class QuizBrain:
    def __init__(self, q_list):
        # Keeps track of the current question number
        self.question_number = 0

        # Stores the list of Question objects
        self.question_list = q_list

        # Tracks the user's score
        self.score = 0

    def still_has_questions(self):
        # Returns True if there are still unanswered questions
        return self.question_number < len(self.question_list)

    def next_question(self):
        # Retrieves the current question based on question_number
        current_question = self.question_list[self.question_number]

        # Move to the next question for the next iteration
        self.question_number += 1

        # Prompt the user for an answer
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        )

        # Check the user's answer against the correct answer
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        # Compare user input with the correct answer (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")

        # Provide immediate feedback after each question
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
