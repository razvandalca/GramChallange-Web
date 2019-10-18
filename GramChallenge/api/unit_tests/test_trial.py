import unittest


class TrialTest(unittest.TestCase):
    def test_passes(self):
        self.assertEqual(self.TEST_NAME, "HEY")

    def setUp(self):
        self.TEST_NAME = "HEY"
