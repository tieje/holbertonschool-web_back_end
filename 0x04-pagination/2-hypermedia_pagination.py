#!/usr/bin/env python3
'''2. Hypermedia pagination mandatory'''
import csv
import math
from optparse import Option
from typing import List, Optional, Tuple, TypedDict


class HyperType(TypedDict, total=False):
    '''Return Dict type for get_hyper() method'''
    page: int
    page_size: int
    data: Optional[List[List]]
    next_page: Optional[int]
    prev_page: Optional[int]
    total_pages: int


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> HyperType:
        '''Return Dictionary of type HyperType'''
        # assertion for variable checking
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        # initializing variables
        pRange: Tuple[(int, int)] = self.index_range(page, page_size)
        dataSet: List[List] = self.dataset()
        totalRows: int = len(dataSet)
        totalPages: int = math.ceil(totalRows / page_size)
        pageSet: Optional[List[List]] = []
        nextPage: Optional[int] = None
        prevPage: Optional[int] = None
        pageSize: int = 0
        # variable mutation depending if statements
        if pRange[1] < totalRows:
            pageSet = [list(dataSet[row])
                       for row in range(pRange[0], pRange[1])]
        if page <= totalPages:
            pageSize = page_size
        if page < totalPages:
            nextPage = page + 1
        if page > 1:
            prevPage = page - 1
        return {
            'page_size': pageSize,
            'page': page,
            'data': pageSet,
            'next_page': nextPage,
            'prev_page': prevPage,
            'total_pages': totalPages
        }

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[(int, int)]:
        '''Return tuple of start and end page'''
        end: int = page * page_size
        start: int = end - page_size
        res = (start, end)
        return res
