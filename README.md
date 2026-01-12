# Project-17---Quiz-Game

This is a beginner-to-intermediate Python project built as part of my 100 Days of Code challenge.

The goal of this project is to build a command-line True/False quiz game using Object-Oriented Programming, where questions are asked sequentially, answers are validated, and a final score is calculated.

**Project Overview**

The Quiz Game allows the user to:

Answer a series of True/False questions

Receive immediate feedback after each question

Track their score throughout the quiz

View a final score summary at the end

The project uses multiple Python classes to separate responsibilities such as question modeling, quiz logic, and data storage.

**Why this project exists**

This project was designed to strengthen my understanding of OOP fundamentals, especially how objects interact across multiple files.

It helped me practice converting raw data into objects and managing program state (score, progress, questions) in a clean and scalable way.

**What I learned**

How to model real-world concepts using classes

How to pass data between objects

How to manage state inside a class (score, current question)

How to split a project across multiple Python files

How to loop through structured data using objects

How to build reusable and extendable program logic

**How the code works (step-by-step)**

Question data is stored as dictionaries inside data.py.

Each dictionary is converted into a Question object containing text and answer.

All Question objects are stored in a question bank list.

The QuizBrain class controls question flow, user input, scoring, and progress tracking.

The quiz continues until there are no questions left.

A final score summary is displayed at the end.

**Project File Structure**

├── main.py              # Program entry point and game loop

├── data.py              # Question data source

├── question_model.py    # Question class definition

├── quiz_brain.py        # Quiz logic and score tracking

**Example Output**

Q.1: The Windows ME operating system was released in the year 2000. (True/False)?:

True

You got it right!

The correct answer was: True

Your current score is: 1/1

...

You've completed the quiz
Your final score was 7/10
