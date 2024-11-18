import unittest
from Main import WordleInfoTheory


class TestWordleInfoTheory(unittest.TestCase):
    def setUp(self):
        self.game = WordleInfoTheory()

    def test_word_length(self):
        self.assertEqual(self.game.word_length, 5)

    def test_max_attempts(self):
        self.assertEqual(self.game.max_attempts, 6)

    def test_word_list_validity(self):
        for word in self.game.word_list:
            self.assertEqual(len(word), 5)
            self.assertTrue(word.isalpha())
            self.assertEqual(word, word.lower())

    def test_feedback_generation(self):
        # Test exact match
        self.assertEqual(self.game.get_feedback("hello", "hello"), "🟩🟩🟩🟩🟩")

        # Test no match
        self.assertEqual(self.game.get_feedback("aaaaa", "bbbbb"), "⬜⬜⬜⬜⬜")

        # Test partial match
        self.assertEqual(self.game.get_feedback("hello", "world"), "⬜⬜🟨⬜⬜")

    def test_entropy_calculation(self):
        entropy = self.game.calculate_entropy("hello", ["hello", "world", "below"])
        self.assertGreater(entropy, 0)

    def test_best_guess(self):
        self.game.possible_words = ["hello", "world", "below"]
        best_guess = self.game.get_best_guess()
        self.assertIn(best_guess, self.game.word_list)


if __name__ == '__main__':
    unittest.main()