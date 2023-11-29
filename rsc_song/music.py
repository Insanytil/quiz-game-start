import pygame


import pygame


class Music:
    def __init__(self):
        self.correct_song_path = "rsc_song/correct-6033.mp3"
        self.wrong_song_path = "rsc_song/negative_beeps-6008.mp3"
        self.volume = 0.2

    def play_wrong_sound(self):
        pygame.init()
        pygame.mixer.init()

        sound = pygame.mixer.Sound(self.wrong_song_path)
        sound.set_volume(self.volume)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))

    def play_correct_sound(self):
        pygame.init()
        pygame.mixer.init()

        sound = pygame.mixer.Sound(self.correct_song_path)
        sound.set_volume(self.volume)
        sound.play()
        pygame.time.delay(int(sound.get_length() * 1000))