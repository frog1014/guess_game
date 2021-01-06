import unittest
import script

class TestGame(unittest.TestCase):
    def test_input(self):
        result = script.run_game(9,9)
        self.assertTrue(result)

    def test_input_wrong(self):
        result = script.run_game('df',9)
        self.assertFalse(result)



if __name__ == '__main__':
    unittest.main()
