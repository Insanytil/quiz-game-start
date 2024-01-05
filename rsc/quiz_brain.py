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
        PRE : - q_list : reçoit une liste d'objets qui doit correspondre à un format spécifique 
        POST : Initialise un objet qui reçoit une liste d'objet,
               la liste reçue doit être formatée de manière spécifique (clés/valeurs)
               afin que le quizz brain puisse les utiliser
               définit les valeurs des paramètres suivant
               cela permettra d'afficher correctement les informations pour le joueur


        """
        self.q_number = 0
        self.q_list = q_list
        self.q_score = 0
        self.music = music.Music()

    def next_question(self):
        '''
        PRE: q_list doit être une liste d'objets à format spécifique
        Charge la question suivante ainsi que ses propositions

        '''
        current_question = self.q_list[self.q_number]
        answers = [html.unescape(current_question[self.CORRECT_ANSWER_TAG])]
        for i in current_question[self.INCORRECT_ANSWER_TAG]:
            answers.append(html.unescape(i))
        random.shuffle(answers)

        print(f"Question {self.q_number + 1}: "
              f"{html.unescape(current_question[self.QUESTION_TAG])}")
        for index, item in enumerate(answers):
            print(f"   {index + 1} : {item}\n")
        user_answer = int(input("Enter the number of the answer : "))

        if user_answer <= len(answers) and user_answer > 0:
            self.q_number += 1
            return self.checking_answer(
            user_answer, answers, html.unescape(current_question[self.CORRECT_ANSWER_TAG]))
        else:
            raise ValueError

    def is_not_last_question(self) -> bool:
        '''
        Vérifie si il y a encore une question
        :return: bool
        '''
        return len(self.q_list) > self.q_number

    def checking_answer(self, user_answer, answer, question_answer):
        '''
        PRE : Recoit l'input int du user avec liste de réponse possible et la réponse correcte
        de la question
        :param user_answer: int
        :param answer: str
        :param question_answer: str
        POST : Affiche si la réponse donnée est correcte ou non par rapport aux paramètres reçu
                Incrément la valeur de self.__q_score si la réponse donnée est correcte
                Joue un son en fonction de la réponse donnée (correcte ou non)
        :return: None
        '''
        if user_answer - 1 == answer.index(html.unescape(question_answer)):
            print('Correct.')
            self.music.play_correct_sound()
            self.q_score += 1
        else:
            self.music.play_wrong_sound()
            print('Wrong.')

        print(f"""
        The correct answer is \033[32m{question_answer}\033[0m.
        Your actual score is {self.q_score}/{self.q_number}.
        
        """)

    def show_final_score(self):
        '''
        Affiche le message de  score final en fonction du score
        '''
        if self.q_score == self.q_number:
            print(f"""
            You have completed the quizz with a score of {self.q_score}/{self.q_number}.
            What a stunning performance ! Congratulations. """)

        if self.q_number > self.q_score >= (self.q_number / 10) * 8:
            print(f"""
            You have completed the quizz with a score of {self.q_score}/{self.q_number}.
            It was almost perfect ! Congratulations. """)

        if (self.q_number / 10) * 8 > self.q_score > (self.q_number / 10) * 5:
            print(f"""
            You have completed the quizz with a score of {self.q_score}/{self.q_number}.
            More than one question in two correct, if it were an exam you would  probably have passed !
            Congratulations. """)

        if (self.q_number / 10) * 5 == self.q_score:
            print(f"""
            You have completed the quizz with a score of {self.q_score}/{self.q_number}.
            Just the Half... Not good, not bad !
            Congratulations. """)
        if (self.q_number / 2) > self.q_score:
            print(f"""
            You have completed the quizz with a score of {self.q_score}/{self.q_number}.
            Ouch not even the half, you will do better next time do not worry  !
            Congratulations. """)
