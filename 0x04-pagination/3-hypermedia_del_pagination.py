#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List, Optional, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        '''Return Dictionary of indexed dataset'''
        # Access Data
        indexedDataSet: Dict[int, List] = self.indexed_dataset()
        totalRows: int = len(indexedDataSet)
        # assertion for variable checking
        assert type(index) is int and type(page_size) is int
        assert index > 0 and page_size > 0
        assert index <= totalRows
        # initializing variables
        pageDataSet: List = []
        nextIndex: Optional[int] = None
        if index + page_size <= totalRows:
            nextIndex = index + page_size
        else:
            nextIndex = totalRows
        # mutations
        rows = 0
        counter = 0
        for i in self.__indexed_dataset.items():
            if rows >= page_size:
                nextIndex = i[0]
                break
            if counter >= index:
                pageDataSet.append(i[1])
                rows += 1
            counter += 1
        return {
            'index': index,
            'data': pageDataSet,
            'page_size': page_size,
            'next_index': nextIndex,
        }
