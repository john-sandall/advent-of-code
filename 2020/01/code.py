"""Advent of Code 2020 - Day 1.

https://adventofcode.com/2020/day/1
"""

from pathlib import Path
from typing import List, Union

import pandas as pd


def load_data(input_filepath: Union[str, Path]) -> List[int]:
    """Load expenses from file and return as Python list.

    Args:
        input_filepath: Location of input file (can be str or pathlib.Path)

    Returns:
        List of integer expense values.
    """
    return pd.read_csv(input_filepath, header=None)[0].to_list()


def part_1(expenses: List[int]) -> int:
    """Find the two entries in expenses that sum to 2020 and return their product.

    Args: expenses: List of integer expense values.

    Returns: Integer product of two entries that sum to 2020.
    """
    return [a * b for a in expenses for b in expenses[expenses.index(a) :] if a + b == 2020][0]


def part_2(expenses: List[int]) -> int:
    """Find the three entries in expenses that sum to 2020 and return their product.

    Args:
        expenses: List of integer expense values.

    Returns:
        Integer product of three entries that sum to 2020.
    """
    return {
        a * b * c for a in expenses for b in expenses for c in expenses if a + b + c == 2020
    }.pop()


if __name__ == "__main__":
    expenses = load_data(input_filepath="input.txt")
    print(part_1(expenses))
    print(part_2(expenses))
