import unittest, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from intervals import merge_intervals


class TestMergeIntervals(unittest.TestCase):
    def test_basic_overlap(self):
        self.assertEqual(merge_intervals([[1, 3], [2, 6], [8, 10]]), [[1, 6], [8, 10]])

    def test_nested_interval(self):
        self.assertEqual(merge_intervals([[1, 5], [2, 3]]), [[1, 5]])

    def test_touching(self):
        self.assertEqual(merge_intervals([[1, 4], [4, 5]]), [[1, 5]])

    def test_unsorted(self):
        self.assertEqual(merge_intervals([[8, 10], [1, 3], [2, 6]]), [[1, 6], [8, 10]])

    def test_no_overlap(self):
        self.assertEqual(merge_intervals([[1, 2], [3, 4]]), [[1, 2], [3, 4]])

    def test_empty(self):
        self.assertEqual(merge_intervals([]), [])


if __name__ == "__main__":
    unittest.main()
