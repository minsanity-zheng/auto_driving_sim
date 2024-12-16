import unittest
from auto_driving_sim import rotate_left, rotate_right, move_forward, is_within_bounds, is_name_existed, is_position_occupied

class TestUtils(unittest.TestCase):
    def test_rotate_left(self):
        self.assertEqual(rotate_left('N'), 'W')
        self.assertEqual(rotate_left('W'), 'S')
        self.assertEqual(rotate_left('S'), 'E')
        self.assertEqual(rotate_left('E'), 'N')

    def test_rotate_right(self):
        self.assertEqual(rotate_right('N'), 'E')
        self.assertEqual(rotate_right('E'), 'S')
        self.assertEqual(rotate_right('S'), 'W')
        self.assertEqual(rotate_right('W'), 'N')

    def test_move_forward(self):
        self.assertEqual(move_forward(0, 0, 'N'), (0, 1))
        self.assertEqual(move_forward(0, 0, 'E'), (1, 0))
        self.assertEqual(move_forward(1, 1, 'S'), (1, 0))
        self.assertEqual(move_forward(1, 1, 'W'), (0, 1))

    def test_is_within_bounds(self):
        self.assertTrue(is_within_bounds(0, 0, 10, 10))
        self.assertTrue(is_within_bounds(9, 9, 10, 10))
        self.assertFalse(is_within_bounds(-1, 0, 10, 10))
        self.assertFalse(is_within_bounds(0, -1, 10, 10))
        self.assertFalse(is_within_bounds(10, 10, 10, 10))

    def test_is_name_existed(self):
        self.assertTrue(is_name_existed('A', [{'name': 'A'},{'name': 'B'}]))
        self.assertFalse(is_name_existed('C', [{'name': 'A'},{'name': 'B'}]))

    def test_is_position_occupied(self):
        self.assertTrue(is_position_occupied(5, 5, [{'x': 5,'y': 5}]))
        self.assertFalse(is_position_occupied(4, 5, [{'x': 5,'y': 5}]))
        self.assertFalse(is_position_occupied(5, 4, [{'x': 5,'y': 5}]))
        self.assertFalse(is_position_occupied(4, 4, [{'x': 5,'y': 5}]))

if __name__ == "__main__":
    unittest.main()
