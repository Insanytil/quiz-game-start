import html
import random
from rsc_song import music


class QuizBrain:
    """
    Créer un nouveau quiz pour jouer
    """
# Initialisation des constantes nécessaires
    CORRECT_ANSWER_TAG = 'correct_answer'
    INCORRECT_ANSWER_TAG = 'incorrect_answers'
    QUESTION_TAG = 'question'

    def __init__(self, q_list: list[object]):
        """
        initialise le un nouveau quiz
        PRE : - q_list :


        """
        self.q_number = 0
        self.q_list = q_list
        self.q_score = 0
        self.music = music.Music()

    def next_question(self):
        current_question = self.q_list[self.q_number]
        answers = [html.unescape(current_question[self.CORRECT_ANSWER_TAG])]
        for i in current_question[self.INCORRECT_ANSWER_TAG]:
            answers.append(html.unescape(i))
        random.shuffle(answers)

        print(f"Question {self.q_number + 1}: {html.unescape(current_question[self.QUESTION_TAG])}")
        for index, item in enumerate(answers):
            print(f"   {index + 1} : {item}\n")
        try:
            user_answer = int(input("Enter the number of the answer : "))
            if user_answer > len(answers):
                raise ValueError
        except ValueError:
            print('Please enter valid number')
            return self.next_question()
        self.q_number += 1

        return self.checking_answer(user_answer, answers, html.unescape(current_question[self.CORRECT_ANSWER_TAG]))

    def is_not_last_question(self) -> bool:
        return len(self.q_list) > self.q_number

    def checking_answer(self, user_answer, answer, question_answer):
        if user_answer - 1 == answer.index(html.unescape(question_answer)):
            print('Correct.')
            self.music.play_correct_sound()
            self.q_score += 1
        else:
            self.music.play_wrong_sound()
            print('Wrong.')

        print(f"""
        The correct answer is {question_answer}.
        Your actual score is {self.q_score}/{self.q_number}.
        
        """)

    def show_final_score(self):
        if self.q_score == self.q_number:
            print(f"""
            You've completed the quizz with a score of {self.q_score}/{self.q_number}.
            What a stunning performance ! Congratulations. """)

        if self.q_number > self.q_score >= (self.q_number / 10)*8:
            print(f"""
            You've completed the quizz with a score of {self.q_score}/{self.q_number}.
            It was almost perfect ! Congratulations. """)

        if (self.q_number / 10) * 8 > self.q_score > (self.q_number / 10) * 5:
            print(f"""
            You've completed the quizz with a score of {self.q_score}/{self.q_number}.
            More than one question in two correct, if it were an exam you'd probably have passed !
            Congratulations. """)

        if (self.q_number / 10) * 5 == self.q_score:
            print(f"""
            You've completed the quizz with a score of {self.q_score}/{self.q_number}.
            Just the Half... Not good, not bad !
            Congratulations. """)
        if (self.q_number / 2) > self.q_score:
            print(f"""
            You've completed the quizz with a score of {self.q_score}/{self.q_number}.
            Ouch not even the half, you'll do better next time don't worry  !
            Congratulations. """)
