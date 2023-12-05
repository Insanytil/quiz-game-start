import json
import requests


class Data:
    """
    Défini les datas nécessaires pour jouer
    
    """
    def __init__(self, amount: int, difficulty: str, type_question: str, categ: int):
        """
        PRE: - amount : integer représentant le nombre de questions demandées par le joueur
             - difficulty : str représentant le choix de le difficulté par le joueur
             - type_question : str représentant le type de question (qcm only pour le moment)
             - categ : int représentant le nombre définissant la catégorie choisie par le joueur
        

        POST: Initialise un objet data qui permettra d'être utilisée par le quizzBrain si les
        valeurs ont été correctement introduites dans le pré
        """
        self.amount = amount
        self.difficulty = difficulty
        self.type_question = type_question
        self.categorie = categ

    def get_random_questions(self):
        """
        Effectue une requête http (get) pour récuperer des données en format JSON
        """
# Utilisation de la lib requests pour pouvoir addresser
# une requête web au serveur de opendb.com afin
# de générer une API et récolter des données utilisables pour le quizz
        response = requests.get(f"https://opentdb.com/api.php?"
            f"amount={self.amount}&category={self.categorie}&difficulty={self.difficulty}"
            f"&type={self.type_question}", timeout=15)
        if response.status_code == 200:
            open_trivia_data = json.loads(response.text)
            return open_trivia_data['results']
        print(f"Erreur lors de la récupération des questions: {response.status_code}")
        return None
