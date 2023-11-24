import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.assertTrue(True, 'Example assertion.')
        
    def test_crash_invalid_operations(self):
        """
        Each of these conditions will cause a crash in the quizzes module due to an invalid operation as a result of an unexpected argument being passed in.
        e.g. addition is not valid between dictionaries and strings. Line 63 of quizzes_controller.py
        """

        quiz_id = self.ctrl.add_quiz({"title": "title", "text": "quiz description", "available_date": 1, "hello": 2}, "quiz description", 1, 2)
        quiz_id = self.ctrl.add_quiz(1, "quiz description", 1, 2)
        quiz_id = self.ctrl.add_quiz(1.1, "quiz description", 1, 2)
        quiz_id = self.ctrl.add_quiz(b"s", "quiz description", 1, 2)

    def test_crash_non_serializable(self):
        """
        Each of these conditions will cause a crash in the quizzes module due to an unexpected parameter that was passed. The passed parameter in these examples
        is a bytes value and is not serializable by the json.dumps operation in save_data.
        """
        
        quiz_id = self.ctrl.add_quiz("title", b"quiz description", 1, 2)
        question_id = self.ctrl.add_question(quiz_id, "q_title", "q_body")  # setup
        self.ctrl.add_answer(question_id, b"\x41", True)

if __name__ == '__main__':
    unittest.main()