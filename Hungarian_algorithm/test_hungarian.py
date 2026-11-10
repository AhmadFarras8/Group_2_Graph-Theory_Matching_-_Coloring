import itertools
import random
import unittest

from hungarian import hungarian, read_matrix


def brute_force(cost):
    n = len(cost)
    return min(sum(cost[i][p[i]] for i in range(n))
               for p in itertools.permutations(range(n)))


class TestHungarian(unittest.TestCase):
    def test_lecture_bulldozer_example(self):
        cost = [[90, 75, 75, 80], [35, 85, 55, 65],
                [125, 95, 90, 105], [45, 110, 95, 115]]
        assignment, total = hungarian(cost)
        self.assertEqual(total, 275)
        self.assertEqual(assignment, [3, 2, 1, 0])

    def test_one_by_one(self):
        self.assertEqual(hungarian([[7]]), ([0], 7))

    def test_identity_costs(self):
        cost = [[0, 5, 5], [5, 0, 5], [5, 5, 0]]
        self.assertEqual(hungarian(cost)[1], 0)

    def test_all_equal_costs(self):
        cost = [[3] * 4 for _ in range(4)]
        self.assertEqual(hungarian(cost)[1], 12)

    def test_assignment_is_permutation(self):
        cost = [[4, 1, 3], [2, 0, 5], [3, 2, 2]]
        assignment, _ = hungarian(cost)
        self.assertEqual(sorted(assignment), [0, 1, 2])

    def test_random_matrices_match_brute_force(self):
        random.seed(11)
        for n in range(1, 8):
            for _ in range(25):
                cost = [[random.randint(0, 50) for _ in range(n)] for _ in range(n)]
                self.assertEqual(hungarian(cost)[1], brute_force(cost))

    def test_read_matrix(self):
        self.assertEqual(read_matrix(["2 # size", "1 2", "3 4"]),
                         [[1.0, 2.0], [3.0, 4.0]])

    def test_read_matrix_wrong_count(self):
        with self.assertRaises(ValueError):
            read_matrix(["3", "1 2 3", "4 5 6"])


if __name__ == "__main__":
    unittest.main()
