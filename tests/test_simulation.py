import unittest
from auto_driving_sim import run_simulation

class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.field = {'width': 10, 'height': 10}
        self.two_cars_collision = [{'name': 'A', 'x': 0, 'y': 0, 'direction': 'E', 'commands': 'FFLFFFFR'}, {'name': 'B', 'x': 1, 'y': 0, 'direction': 'N', 'commands': 'RFFLFFFFF'}]
        self.two_cars_no_collision = [{'name': 'A', 'x': 0, 'y': 0, 'direction': 'E', 'commands': 'FFLFFFFR'}, {'name': 'B', 'x': 1, 'y': 0, 'direction': 'N', 'commands': 'FFFLFFFFF'}]
        self.three_cars_collision = [{'name': 'A', 'x': 0, 'y': 0, 'direction': 'E', 'commands': 'FFLFFFFR'}, {'name': 'B', 'x': 1, 'y': 0, 'direction': 'N', 'commands': 'RFFLFFFFF'}, {'name': 'C', 'x': 8, 'y': 8, 'direction': 'S', 'commands': 'FFFFFFFFRFFFFFFFFFLF'}]
        
    def test_run_simulation(self):
        self.assertEqual(run_simulation(self.field,self.two_cars_collision), [['A', True, ['B'], 1, 0, 1], ['B', True, ['A'], 1, 0, 1]])
        self.assertEqual(run_simulation(self.field,self.two_cars_no_collision), [['A', False, 2, 4, 'E'], ['B', False, 0, 3, 'W']])
        self.assertEqual(run_simulation(self.field,self.three_cars_collision), [['A', True, ['B'], 1, 0, 1], ['B', True, ['A'], 1, 0, 1], ['C', True, ['A', 'B'], 1, 0, 16]])

if __name__ == "__main__":
    unittest.main()
