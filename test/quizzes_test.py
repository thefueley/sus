import unittest
from datetime import datetime

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')

    def test_add_quiz(self):
        """
        Create a quiz with an invalid title
        """
        # create a quiz with an integer value for the title.
        # This will crash the program at line 63 in app/controllers/quizzes_controller.py
        quiz_id = self.ctrl.add_quiz(3, "", "", "")

if __name__ == '__main__':
    unittest.main()