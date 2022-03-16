import unittest
from ..bowling import GetScore


class MyTest(unittest.TestCase):

    def test_normal(self):
        game_result = 'X12125123533444XX'
        get_score = GetScore(game_result=game_result, new_rules=False)
        game_score = get_score.run()
        self.assertEqual(game_score, 100)

    def test_normal_new_rules(self):
        game_result = 'X12125123533444XX'
        get_score = GetScore(game_result=game_result, new_rules=True)
        game_score = get_score.run()
        self.assertEqual(game_score, 83)

    def test_length(self):
        game_result = '12512512532456345743587568745685484568'
        get_score = GetScore(game_result=game_result, new_rules=False)
        with self.assertRaises(Exception):
            get_score.run()

    def test_excess_symbols(self):
        game_result = '@12125123533444XX22'
        get_score = GetScore(game_result=game_result, new_rules=True)
        with self.assertRaises(Exception):
            get_score.run()

    def test_frame_spare_position(self):
        game_result = 'X/2125123533444XX'
        get_score = GetScore(game_result=game_result, new_rules=True)
        with self.assertRaises(Exception):
            get_score.run()

    def test_frame_points(self):
        game_result = 'X82125123533444XX'
        get_score = GetScore(game_result=game_result, new_rules=True)
        with self.assertRaises(Exception):
            get_score.run()

    def test_strike_position(self):
        game_result = 'X2X21251235334444X1'
        get_score = GetScore(game_result=game_result, new_rules=True)
        with self.assertRaises(Exception):
            get_score.run()

    def test_frame_len(self):
        game_result = '1122334433221112X3'
        get_score = GetScore(game_result=game_result, new_rules=True)
        with self.assertRaises(Exception):
            get_score.run()


if __name__ == '__main__':
    unittest.main()
