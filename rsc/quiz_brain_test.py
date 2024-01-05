import unittest
from unittest.mock import patch
import quiz_brain as quiz




class TestQuizBrain(unittest.TestCase):
    def setUp(self):
        self.q_list = [
            {
                'question': 'What is the capital of France?',
                'correct_answer': 'Paris',
                'incorrect_answers': ['Berlin', 'London', 'Madrid']
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'correct_answer': 'Mars',
                'incorrect_answers': ['Earth', 'Jupiter', 'Saturn']
            }
        ]
        self.quiz_brain_instance = quiz.QuizBrain(self.q_list)
        self.quiz_brain_instance.music.wrong_song_path = "../rsc_song/negative_beeps-6008.mp3"
        self.quiz_brain_instance.music.correct_song_path = "../rsc_song/correct-6033.mp3"

    def test_constructor(self):
        self.assertEqual(self.quiz_brain_instance.q_number, 0, 'q_number not eq to 0')
        self.assertEqual(self.quiz_brain_instance.q_list, self.q_list, 'q_list error')
        self.assertEqual(self.quiz_brain_instance.q_score, 0, 'q_score not eq to 0')
        self.assertIsInstance(self.quiz_brain_instance.music, quiz.music.Music, 'music not an instance of Music')

    @patch('builtins.input', return_value='1')
    @patch('builtins.print')
    @patch('pygame.mixer.Sound')
    def test_display_next_question(self, mock_sound, mock_print, _):
        q_numb = self.quiz_brain_instance.q_number
        self.quiz_brain_instance.next_question()
        self.assertTrue(mock_print.called)
        mock_sound.return_value.play.assert_called_once()
        self.assertIn('Question 1: What is the capital of France?', mock_print.call_args_list[0][0][0])
        self.assertTrue(q_numb + 1, self.quiz_brain_instance.q_number)

    @patch('builtins.input', return_value='5')
    @patch('builtins.print')
    def test_display_next_question_int(self, mock_print, _):
        q_numb = self.quiz_brain_instance.q_number
        with self.assertRaises(ValueError, msg='ValueError not raised'):
            self.quiz_brain_instance.next_question()
            self.assertTrue(mock_print.called)
            self.assertEqual(q_numb, self.quiz_brain_instance.q_number)

    @patch('builtins.input', return_value='0')
    @patch('builtins.print')
    def test_display_next_question_zero(self, mock_print, _):
        q_numb = self.quiz_brain_instance.q_number
        with self.assertRaises(ValueError, msg='ValueError not raised'):
            self.quiz_brain_instance.next_question()
            self.assertTrue(mock_print.called)
            self.assertEqual(q_numb, self.quiz_brain_instance.q_number)

    @patch('builtins.input', return_value='m')
    @patch('builtins.print')
    def test_display_next_question_string(self, mock_print, _):
        q_numb = self.quiz_brain_instance.q_number
        with self.assertRaises(ValueError, msg='ValueError not raised'):
            self.quiz_brain_instance.next_question()
            self.assertTrue(mock_print.called)
            self.assertEqual(q_numb, self.quiz_brain_instance.q_number)

    def test_is_not_last_question(self):
        q_list = [{'q1': 'test'}]
        new_instance = quiz.QuizBrain(q_list)
        new_instance.q_number = 1
        self.assertFalse(new_instance.is_not_last_question())
        q_list = [{}]
        new_instance = quiz.QuizBrain(q_list)
        new_instance.q_number = 0
        self.assertTrue(new_instance.is_not_last_question())
        q_list = []
        new_instance = quiz.QuizBrain(q_list)
        new_instance.q_number = 0
        self.assertFalse(new_instance.is_not_last_question())
        q_list = [{'q1': 'test'}, {'q2': 'test'}]
        new_instance = quiz.QuizBrain(q_list)
        new_instance.q_number = 0
        self.assertTrue(new_instance.is_not_last_question())
        new_instance.q_number = 1
        self.assertTrue(new_instance.is_not_last_question())
        new_instance.q_number = 2
        self.assertFalse(new_instance.is_not_last_question())

    @patch('quiz_brain.music.Music.play_correct_sound')
    @patch('builtins.print')
    def test_checking_answer_test(self, mock_print,mock_play):
        q_score = self.quiz_brain_instance.q_score
        self.quiz_brain_instance.checking_answer(1, ['Paris', 'London', 'Madrid', 'Berlin'],
    'Paris')
        self.assertEqual(self.quiz_brain_instance.q_score, q_score + 1, 'Q_score not +1')
        mock_play.assert_called_once()
        mock_print.assert_called()
        self.assertEqual(mock_print.call_count, 2)

    @patch('quiz_brain.music.Music.play_wrong_sound')
    @patch('builtins.print')
    def test_checking_incorrect_answer(self, mock_print, mock_play):
        q_score = self.quiz_brain_instance.q_score
        self.quiz_brain_instance.checking_answer(1, ['Madrid', 'Paris', 'London', 'Berlin'],
    'Paris')
        self.assertEqual(self.quiz_brain_instance.q_score, q_score, 'Q_score changed')
        mock_play.assert_called_once()
        mock_print.assert_called()
        self.assertEqual(mock_print.call_count, 2)
    @patch('builtins.print')
    def test_show_final_max_score(self, mock_print):
        self.quiz_brain_instance.q_score = 10
        self.quiz_brain_instance.q_number = 10
        self.quiz_brain_instance.show_final_score()
        mock_print.assert_called_once()
        self.assertIn(f"""
            You have completed the quizz with a score of {self.quiz_brain_instance.q_score}/{self.quiz_brain_instance.q_number}.
            What a stunning performance ! Congratulations. """, mock_print.call_args_list[0][0][0])

    @patch('builtins.print')
    def test_show_final_8_score(self, mock_print):
        self.quiz_brain_instance.q_score = 8
        self.quiz_brain_instance.q_number = 10
        self.quiz_brain_instance.show_final_score()
        mock_print.assert_called_once()
        self.assertIn(f"""
            You have completed the quizz with a score of {self.quiz_brain_instance.q_score}/{self.quiz_brain_instance.q_number}.
            It was almost perfect ! Congratulations. """, mock_print.call_args_list[0][0][0])

    @patch('builtins.print')
    def test_show_final_6_score(self, mock_print):
        self.quiz_brain_instance.q_score = 6
        self.quiz_brain_instance.q_number = 10
        self.quiz_brain_instance.show_final_score()
        mock_print.assert_called_once()
        self.assertIn(f"""
            You have completed the quizz with a score of {self.quiz_brain_instance.q_score}/{self.quiz_brain_instance.q_number}.
            More than one question in two correct, if it were an exam you would  probably have passed !
            Congratulations. """, mock_print.call_args_list[0][0][0])

    @patch('builtins.print')
    def test_show_final_5_score(self, mock_print):
        self.quiz_brain_instance.q_score = 5
        self.quiz_brain_instance.q_number = 10
        self.quiz_brain_instance.show_final_score()
        mock_print.assert_called_once()
        self.assertIn(f"""
            You have completed the quizz with a score of {self.quiz_brain_instance.q_score}/{self.quiz_brain_instance.q_number}.
            Just the Half... Not good, not bad !
            Congratulations. """, mock_print.call_args_list[0][0][0])

    @patch('builtins.print')
    def test_show_final_4_or_under_score(self, mock_print):
        self.quiz_brain_instance.q_score = 4
        self.quiz_brain_instance.q_number = 10
        self.quiz_brain_instance.show_final_score()
        mock_print.assert_called_once()
        self.assertIn(f"""
            You have completed the quizz with a score of {self.quiz_brain_instance.q_score}/{self.quiz_brain_instance.q_number}.
            Ouch not even the half, you will do better next time do not worry  !
            Congratulations. """, mock_print.call_args_list[0][0][0])


if __name__ == '__main__':
    unittest.main()
