import unittest
from unittest.mock import patch, Mock
from get_question import GetQuestion



class TestGetQuestionClass(unittest.TestCase):
    def setUp(self):
        self.amount = 10
        self.difficulty = 'easy'
        self.type_question = 'multiple'
        self.categorie = 9
    def test_constructor(self):

        get_question_instance = GetQuestion(self.amount, self.difficulty, self.type_question, self.categorie)

        self.assertEqual(get_question_instance.amount, self.amount, 'amount is not correct')
        self.assertEqual(get_question_instance.difficulty, self.difficulty, 'difficulty is not correct')
        self.assertEqual(get_question_instance.type_question, self.type_question, 'type_question is not correct')
        self.assertEqual(get_question_instance.categorie, self.categorie, 'categ is not correct')

    @patch('get_question.requests.get')
    def test_successful_request(self, mock_get):
        get_question_instance = GetQuestion(self.amount, self.difficulty, self.type_question, self.categorie)

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = '{"results": [{"question": "Sample question"}]}'
        mock_get.return_value = mock_response

        result = get_question_instance.get_random_questions()
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 1, 'len must be = 1')
        self.assertEqual(result[0]['question'], 'Sample question')

    @patch('get_question.requests.get')
    def test_failed_request(self, mock_get):
        get_question_instance = GetQuestion(self.amount, self.difficulty, self.type_question, self.categorie)

        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_question_instance.get_random_questions()
        self.assertIsNone(result)

    @patch('get_question.requests.get')
    def test_exception_handling(self, mock_get):
        get_question_instance = GetQuestion(self.amount, self.difficulty, self.type_question, self.categorie)

        mock_get.side_effect = Exception("Connection error")

        result = get_question_instance.get_random_questions()
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
