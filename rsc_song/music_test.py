import unittest
from unittest.mock import patch
from music import Music


class TestMusicClass(unittest.TestCase):
    def setUp(self):
        self.music_class = Music()

    def test_constructor(self):
        self.assertEqual(self.music_class.correct_song_path,"rsc_song/correct-6033.mp3",
                         'correct_song_path not found or incorrect')
        self.assertEqual(self.music_class.wrong_song_path, "rsc_song/negative_beeps-6008.mp3",
                         'wrong_song_path not found or incorrect')
        self.assertEqual(self.music_class.volume, 0.2, 'volume is not correct')

    # ----------------WARNING ---------------------------------------------
    # Les mocks sont injectés dans la fonction de test en tant que paramètres
    # dans l'ordre inverse de leur apparition dans le décorateur
    @patch('pygame.mixer.Sound')
    @patch('pygame.time.delay')
    def test_play_correct_sound_calls(self, mock_delay, mock_sound):
        self.music_class.play_correct_sound()
        # Check if pygame.mixer.sound has been initialised with the correct path
        mock_sound.assert_called_once_with("rsc_song/correct-6033.mp3")
        # Check if set_volume has been called with correct value
        mock_sound.return_value.set_volume.assert_called_once_with(0.2)
        # Check if play method has been called
        mock_sound.return_value.play.assert_called_once()
        # Check if pygame.delay has been called with correct timing
        expected_delay = int(mock_sound.return_value.get_length() * 1000)
        mock_delay.assert_called_once_with(expected_delay)

    @patch('pygame.mixer.Sound')
    @patch('pygame.time.delay')
    def test_play_wrong_song_calls(self, mock_delay, mock_sound):
        self.music_class.play_wrong_sound()
        # Check if pygame.mixer.sound has been initialised with the correct path
        mock_sound.assert_called_once_with("rsc_song/negative_beeps-6008.mp3")
        # Check if set_volume has been called with correct value
        mock_sound.return_value.set_volume.assert_called_once_with(0.2)
        # Check if play method has been called
        mock_sound.return_value.play.assert_called_once()
        # Check if pygame.delay has been called with correct timing
        expected_delay = int(mock_sound.return_value.get_length() * 1000)
        mock_delay.assert_called_once_with(expected_delay)


if __name__ == '__main__':
    unittest.main()
