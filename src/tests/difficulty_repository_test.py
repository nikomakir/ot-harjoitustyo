import unittest
from repositories.difficulty_repository import difficulty_repository


class TestDifficultyRepository(unittest.TestCase):
    def setUp(self):
        difficulty_repository.write(0)
        self.difficulty = 50

    def test_write(self):
        difficulty_repository.write(self.difficulty)
        self.assertEqual(self.difficulty, difficulty_repository.load())

    def test_load(self):
        self.assertEqual(difficulty_repository.load(), 0)
