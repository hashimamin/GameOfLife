import unittest
from game_of_life_engine import *


class MyTestCase(unittest.TestCase):
    def test_get_next_state(self):
        init_state1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected_next_state1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(get_next_state(init_state1), expected_next_state1)

        init_state2 = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        expected_next_state2 = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        self.assertEqual(get_next_state(init_state2), expected_next_state2)


if __name__ == '__main__':
    unittest.main()