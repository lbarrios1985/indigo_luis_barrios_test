from typing import List
import unittest

class DataCapture:
    """
    A class used for capturing data and building statistics.

    Attributes
    ----------
    nums : list
        A list of integers representing the captured data.
    counts : list
        A list of integers representing the count of each number in the captured data.

    Methods
    -------
    add(num: int) -> None:
        Adds a number to the captured data and updates the count for that number.
    build_stats() -> Statistics:
        Builds and returns a Statistics object based on the captured data.
    """
    def __init__(self):
        self.nums = []
        self.counts = [0] * 1000  # assuming all numbers will be less than 1000

    def add(self, num: int) -> None:
        self.nums.append(num)
        self.counts[num - 1] += 1  # Increment the count for the added number

    def build_stats(self):
        return Statistics(self.nums, self.counts)

class Statistics:
    """
    A class for calculating statistics on a list of numbers and their counts.

    Attributes:
    -----------
    nums : List[int]
        A list of numbers.
    counts : List[int]
        A list of counts for each number in nums.
    """

    def __init__(self, nums: List[int], counts: List[int]):
        self.nums = nums
        self.counts = counts

    def less(self, value: int) -> int:
        """
        Returns the number of elements in nums that are less than value.

        Parameters:
        -----------
        value : int
            The value to compare against.

        Returns:
        --------
        int
            The number of elements in nums that are less than value.
        """
        return sum(1 for num in self.nums if num < value)
    
    def greater(self, value: int) -> int:
        """
        Returns the sum of counts for all elements in nums that are greater than or equal to value.

        Parameters:
        -----------
        value : int
            The value to compare against.

        Returns:
        --------
        int
            The sum of counts for all elements in nums that are greater than or equal to value.
        """
        return sum(self.counts[value:])

    def between(self, low: int, high: int) -> int:
        """
        Returns the number of elements in nums that are between low and high (inclusive).

        Parameters:
        -----------
        low : int
            The lower bound of the range to compare against.
        high : int
            The upper bound of the range to compare against.

        Returns:
        --------
        int
            The number of elements in nums that are between low and high (inclusive).
        """
        return sum(1 for num in self.nums if low <= num <= high)


class TestDataCapture(unittest.TestCase):
    """
    Class to test the class DataCapture.
    """
    def test_data_capture(self):
        capture = DataCapture()
        for num in [3, 9, 3, 4, 6]:
            capture.add(num)
        stats = capture.build_stats()
        self.assertEqual(stats.less(4), 2)
        self.assertEqual(stats.between(3, 6), 4)
        self.assertEqual(stats.greater(4), 2)

if __name__ == '__main__':
    unittest.main()