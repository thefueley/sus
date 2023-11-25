import unittest

from app.controllers.quizzes_controller import QuizzesController


class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')

    # quizzes_controller.py Line 63
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.ctrl.clear_data()
        with self.assertRaises(Exception):
            self.ctrl.add_quiz(
                None, None, None, None)

    # utils.py Line 11
    def test_expose_failure_02(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.ctrl.clear_data()

        with self.assertRaises(Exception):
            quiz_id = self.ctrl.add_quiz("A", "B", 1, 1)
            self.ctrl.add_question(quiz_id, '\udbff\udfff', "D")

    # data_loader.py Line 21
    def test_expose_failure_03(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.ctrl.clear_data()

        with self.assertRaises(Exception):
            quiz_id = self.ctrl.add_quiz("A", "B", 1, 1)
            self.ctrl.add_question(quiz_id, b"some binary string", "D")


if __name__ == '__main__':
    unittest.main()
