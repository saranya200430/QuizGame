class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer  # correct_answer should be index (e.g., 2)

    def check_answer(self, user_answer_index):
        return user_answer_index == self.correct_answer

class QuizGame:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def play(self):
        for question in self.questions:
            print("\n" + question.question)
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")
            user_choice = input("Enter the number of your answer: ")
            try:
                user_choice = int(user_choice)
                if 1 <= user_choice <= len(question.options):
                    if question.check_answer(user_choice-1):
                        print("Correct!\n")
                        self.score += 1
                    else:
                        print("Incorrect!\n")
                else:
                    print("Choice out of range.\n")
            except ValueError:
                print("Invalid choice. Please choose a valid option.\n")
        print(f"Quiz complete! Your score: {self.score}/{len(self.questions)}")


# List of questions
questions = [
    Question(
        "Who developed Python Programming Language?",
        ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene Stom"],
        3 #Guido van Rossum
    ),
    Question(
        "Which type of Programming does Python support?",
        ["Object-oriented programming", "Structured programming", "Functional programming", "All of the mentioned"],
        4 #All of the mentioned
    ),
    Question(
        "Is Python case sensitive when dealing with identifiers?",
        ["no", "yes", "machine dependent", "none of the mentioned"],
        2 #yes
    ),
    Question(
        "Which of the following is the correct extension of the Python file?",
        [".python", ".pl", ".py", ".p"],
        3 #.py
    ),
    Question(
        "Is Python code compiled or interpreted?",
        ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted", "Python code is only compiled", "Python code is only interpreted"],
        1 #Python code is both compiled and interpreted
    ),
    Question(
        "All keywords in Python are in _________?",
        ["Capitalized", "lower case", "UPPER CASE", "None of the mentioned"],
        1 #Capitalized
    ),
    Question(
        "What will be the value of the following Python expression? `2**3`",
        ["7", "2", "8", "1"],
        1 #7
    ),
    Question(
        "Which of the following is used to define a block of code in Python language?",
        ["Indentation", "Key", "Fun", "Define"],
        1 #Indentation
    ),
    Question(
        "Which keyword is used for function in Python language?",
        ["Function", "def", "Fun", "Define"],
        2 #def
    ),
    Question(
        "Which of the following character is used to give single-line comments in Python?",
        ["//", "#", "!", "/*"],
        2 
    )
]

# Initialize and play quiz
quiz = QuizGame(questions)
quiz.play()
