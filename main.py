from rsc .get_question import GetQuestion
from rsc .quiz_brain import QuizBrain
import os

if __name__ == "__main__":
    def play_game():
        """
        Initialise les paramètres en récoltant les données nécessaires au jeu et le joue
        :return:
        """
        correct_amount_value: bool = False
        correct_difficulty_value: bool = False
        difficulty_mode: tuple = ("easy", "medium", "hard")
        type_question: str = 'multiple'
        categories_book: object = \
            {"Geography": 22, "History": 23, "General Knowledge": 9, "Sciences : Computer": 18}
        categories_name: tuple = \
            ("Geography", "History", "General Knowledge", "Sciences : Computer")
        categories_value: bool = False

        print("Welcome to Lucien's Quizz, choose a category :")

        while not categories_value:
            for index, categ in enumerate(categories_name):
                print(f"{index + 1}) {categ}\n")
            try:
                user_categorie: int = int(input("Choose a category by entering the number\n>>>  "))
                if user_categorie in range(1, len(categories_name) + 1):
                    categories_value = True
                    print(f"Your categorie choice : {categories_name[user_categorie - 1]}")
                else:
                    raise ValueError
            except ValueError:
                print('Enter a valid number')

        while not correct_amount_value:
            try:
                user_amount: int = (int
                    (input('How many questions do you like to have in your quizz :\n>>> ')))
                if user_amount <= 0:
                    print('please insert a valid number (minimum 1) as you went <=0')
                else:
                    correct_amount_value = True
            except ValueError:
                print('Please insert a valid number (minimum is 1).')

        while not correct_difficulty_value:
            try:
                user_difficulty: str = (input
                    ('Choose a difficulty : [Easy/Medium/Hard]\n>>> ').lower())
                if user_difficulty in difficulty_mode:
                    correct_difficulty_value = True
                else:
                    print('Please enter a correct difficulty')
            except ValueError:
                print('Please enter a correct difficulty.')

        new_get_question = GetQuestion(user_amount, user_difficulty, type_question,
                        categories_book[categories_name[user_categorie - 1]])
        new_quiz = QuizBrain(new_get_question.get_random_questions())

        while new_quiz.is_not_last_question():
            try:
                new_quiz.next_question()
            except ValueError:
                print('You must enter [1/2/3/4]')






        new_quiz.show_final_score()
        user_input: str = input("Do you want to play again ? [y/n]").lower()

        if user_input == 'y' or user_input == 'yes':
            # Attention la récursivité en python est limitée !
            os.system('cls')
            play_game()
        else:
            os.system('cls')
            print('Thanks for playing')

play_game()
