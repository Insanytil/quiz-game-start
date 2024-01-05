import pygame


class Music:
    """
    Initialise un objet de class Music
    """
    def __init__(self):
        """
        PRE : Au préalable quand la classe est créée, il faut qu'elle soit créée depuis la position du fichier main
             
        POST : Initialise la class avec les chemins des fichiers audio
               depuis la position du fichier main ssi bien positionné
        """

        self.correct_song_path = "rsc_song/correct-6033.mp3"
        self.wrong_song_path = "rsc_song/negative_beeps-6008.mp3"
        self.volume = 0.2

    def play_wrong_sound(self):
        """
        PRE: Le fichier réprésenter par self.__wrong_song_path doit être un fichier audio et existant,
             le module pygame doit présent dans l'interpréteur
        POST: Permet de jouer le son de réponse incorrecte 
        """
        pygame.init()
        pygame.mixer.init()

        sound = pygame.mixer.Sound(self.wrong_song_path)
        sound.set_volume(self.volume)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))

    def play_correct_sound(self):
        """
        PRE: Le fichier réprésenter par self.correct_song_path doit être un fichier audio et existant,
             le module pygame doit présent dans l'interpréteur
        POST: Permet de jouer le son de réponse correcte
        """
        pygame.init()
        pygame.mixer.init()

        sound = pygame.mixer.Sound(self.correct_song_path)
        sound.set_volume(self.volume)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))
