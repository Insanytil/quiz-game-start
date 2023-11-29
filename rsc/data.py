import json
import requests



class Data:
    """
    Défini les datas nécessaires pour jouer
    
    """
    def __init__(self, amount: int, difficulty: str, type_question: str, categorie: int):
        """
        PRE: 
        

        POST: Initialise un objet data selon les paramètres obtenusw
        """
        self.amount = amount
        self.difficulty = difficulty
        self.type_question = type_question
        self.categorie = categorie
        """"""

    def get_random_questions(self):
        """
        
        """
        # Utilisation de la lib requests pour pouvoir addresser une requête web au serveur de opendb.com afin
        # de générer une API et récolter des données utilisables pour le quizz
        response = requests.get(f"https://opentdb.com/api.php?"
                                f"amount={self.amount}&category={self.categorie}&difficulty={self.difficulty}&type={self.type_question}")
        if response.status_code == 200:
            open_trivia_data = json.loads(response.text)
            return open_trivia_data['results']
        else:
            print(f"Erreur lors de la récupération des questions: {response.status_code}")
            return None



