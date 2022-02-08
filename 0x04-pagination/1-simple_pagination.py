#!/usr/bin/env python3
'''1. Simple pagination'''
import csv
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Return rows of data from csv'''
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        pRange: Tuple[(int, int)] = self.index_range(page, page_size)
        dataset: List[List] = self.dataset()
        if pRange[1] > len(dataset):
            return []
        return [list(dataset[row]) for row in range(pRange[0], pRange[1])]

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[(int, int)]:
        '''Return tuple of start and end page'''
        end: int = page * page_size
        start: int = end - page_size
        res = (start, end)
        return res
