import pygame


class Music:
    """
    Initialise une class Music
    """
    def __init__(self):
        """
        PRE :
        POST : Initialise la class avec les chemins des fichiers audio depuis la racine du fichier main
        """
        self.__correct_song_path = "rsc_song/correct-6033.mp3"
        self.__wrong_song_path = "rsc_song/negative_beeps-6008.mp3"
        self.__volume = 0.2

    def play_wrong_sound(self):
        pygame.init()
        pygame.mixer.init()

        sound = pygame.mixer.Sound(self.__wrong_song_path)
        sound.set_volume(self.__volume)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))

    def play_correct_sound(self):
        pygame.init()
        pygame.mixer.init()

        sound = pygame.mixer.Sound(self.__correct_song_path)
        sound.set_volume(self.__volume)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))
