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
        initialise  un nouveau quiz
        PRE : - q_list : reçoit une liste d'objets
        POST : Initialise un objet qui reçoit une liste d'objet,
               la liste reçue doit être formatée de manière spécifique (clés/valeurs)
               afin que le quizz brain puisse les utiliser


        """
        self.__q_number = 0
        self.__q_list = q_list
        self.__q_score = 0
        self.__music = music.Music()

    def next_question(self):
        '''
        Charge la question suivante ainsi que ses propositions

        '''
        current_question = self.__q_list[self.__q_number]
        answers = [html.unescape(current_question[self.CORRECT_ANSWER_TAG])]
        for i in current_question[self.INCORRECT_ANSWER_TAG]:
            answers.append(html.unescape(i))
        random.shuffle(answers)

        print(f"Question {self.__q_number + 1}: "
              f"{html.unescape(current_question[self.QUESTION_TAG])}")
        for index, item in enumerate(answers):
            print(f"   {index + 1} : {item}\n")
        try:
            user_answer = int(input("Enter the number of the answer : "))
            if user_answer > len(answers) or user_answer == 0:
                raise ValueError
        except ValueError:
            print('Please enter valid number [1/2/3/4]')
            return self.next_question()
        self.__q_number += 1
        return self.checking_answer(
            user_answer, answers, html.unescape(current_question[self.CORRECT_ANSWER_TAG]))

    def is_not_last_question(self) -> bool:
        '''
        Vérifie si il y a encore une question
        :return: bool
        '''
        return len(self.__q_list) > self.__q_number

    def checking_answer(self, user_answer, answer, question_answer):
        '''
        PRE : Recoit l'input int du user avec liste de réponse possible et la réponse correcte
        de la question
        :param user_answer: int
        :param answer: str
        :param question_answer: str
        POST : Affiche si la réponse donnée est correcte ou non par rapport aux paramètres reçu
        :return: None
        '''
        if user_answer - 1 == answer.index(html.unescape(question_answer)):
            print('Correct.')
            self.__music.play_correct_sound()
            self.__q_score += 1
        else:
            self.__music.play_wrong_sound()
            print('Wrong.')

        print(f"""
        The correct answer is {question_answer}.
        Your actual score is {self.__q_score}/{self.__q_number}.
        
        """)

    def show_final_score(self):
        '''
        Affiche le message de  score final en fonction du score
        '''
        if self.__q_score == self.__q_number:
            print(f"""
            You've completed the quizz with a score of {self.__q_score}/{self.__q_number}.
            What a stunning performance ! Congratulations. """)

        if self.__q_number > self.__q_score >= (self.__q_number / 10) * 8:
            print(f"""
            You've completed the quizz with a score of {self.__q_score}/{self.__q_number}.
            It was almost perfect ! Congratulations. """)

        if (self.__q_number / 10) * 8 > self.__q_score > (self.__q_number / 10) * 5:
            print(f"""
            You've completed the quizz with a score of {self.__q_score}/{self.__q_number}.
            More than one question in two correct, if it were an exam you'd probably have passed !
            Congratulations. """)

        if (self.__q_number / 10) * 5 == self.__q_score:
            print(f"""
            You've completed the quizz with a score of {self.__q_score}/{self.__q_number}.
            Just the Half... Not good, not bad !
            Congratulations. """)
        if (self.__q_number / 2) > self.__q_score:
            print(f"""
            You've completed the quizz with a score of {self.__q_score}/{self.__q_number}.
            Ouch not even the half, you'll do better next time don't worry  !
            Congratulations. """)
