#!/usr/bin/env python3
"""
   a function named index_range that takes two
   integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size"""
    index = page * page_size - page_size
    index_ = index + page_size
    return (index, index_)