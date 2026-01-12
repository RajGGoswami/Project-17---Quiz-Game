# Day 17 – Quiz Game
# This file acts as the entry point of the application.
# Its responsibility is to:
# - Prepare question objects
# - Initialize the quiz engine
# - Control the main game loop

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# This list will store Question objects instead of raw data
# Using objects makes the quiz easier to manage and extend
question_bank = []

# Convert each dictionary from question_data into a Question object
# This separates raw data from application logic
for q_dict in question_data:
    q_object = Question(
        q_text=q_dict['question'],
        q_answer=q_dict['correct_answer']
    )
    question_bank.append(q_object)

# Create the QuizBrain object which controls the quiz flow
quiz = QuizBrain(question_bank)

# Main game loop
# Continues asking questions as long as there are questions remaining
while quiz.still_has_questions():
    quiz.next_question()

# Final summary displayed once the quiz is complete
print(f"\n\nYou've completed the quiz\nYour final score was {quiz.score}/{quiz.question_number}")
