# 0x00-pagination

## Definition
Most end-points that return a list of entities will need to have some sort of pagination. Without pagination a simple search could return millions or even billions of hits causing extranous network traffic. Paging requires an implied ordering. By default this may be the item’s unique identifier, but can be other ordered fields such as a created date

1. Offset Pagination
This is the simplest form of paging. Limit/Offset became popular with apps using SQL databases which already have LIMIT and OFFSET as part of the SQL SELECT Syntax. Very little business logic is required to implement Limit/Offset paging.
```
ExamplePermalink

(Assume the query is ordered by created date descending)

    Client makes request for most recent items: GET /items?limit=20
    On scroll/next page, client makes second request GET /items?limit=20&offset=20
    On scroll/next page, client makes third request GET /items?limit=20&offset=40
```

2. Keyset Pagination
Keyset pagination uses the filter values of the last page to fetch the next set of items. Those columns would be indexed.
```
ExamplePermalink

(Assume the query is ordered by created date descending)

    Client makes request for most recent items: GET /items?limit=20
    On scroll/next page, client finds the minimum created date of 2021-01-20T00:00:00 from previously returned results. and then makes second query using date as a filter: GET /items?limit=20&created:lte:2021-01-20T00:00:00
    On scroll/next page, client finds the minimum created date of 2021-01-19T00:00:00 from previously returned results. and then makes third query using date as a filter: GET /items?limit=20&created:lte:2021-01-19T00:00:00
```

3. Seek Pagination
Seek Paging is an extension of Keyset paging. By adding an after_id or start_id URL parameter, we can remove the tight coupling of paging to filters and sorting. Since unique identifiers are naturally high cardinality, we won’t run into issues unlike if sorting by a low cardinality field like state enums or category name.
```
ExamplePermalink

(Assume the query is ordered by created date ascending)

    Client makes request for most recent items: GET /items?limit=20
    On scroll/next page, client finds the last id of ‘20’ from previously returned results. and then makes second query using it as the starting id: GET /items?limit=20&after_id=20
    On scroll/next page, client finds the last id of ‘40’ from previously returned results. and then makes third query using it as the starting id: GET /items?limit=20&after_id=40
```

### RESOURCES
- [REST API Design: Pagination](https://intranet.alxswe.com/rltoken/7Kdzi9CH1LdSfNQ4RaJUQw)
- [HATEOAS](https://intranet.alxswe.com/rltoken/tfzcEbTSdMYSYxsspJH_oA)

### LEARNING OBJECTIVES
~~~
    How to paginate a dataset with simple page and page_size parameters
    How to paginate a dataset with hypermedia metadata
    How to paginate in a deletion-resilient manner
~~~

#### Project Tasks

| Task | Description |
| ---- | ----------- |
|  0. Simple helper function | Write a function named index_range that takes two integer arguments page and page_size; should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters |

1. Simple pagination
Copy `index_range` from the previous task and the following class into your code
```
import csv
import math
from typing import List


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
            pass
```
Implement a method named get_page that takes two integer arguments page with default value 1 and page_size with default value 10.
```
    You have to use this CSV file (same as the one presented at the top of the project)
    Use assert to verify that both arguments are integers greater than 0.
    Use index_range to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
    If the input arguments are out of range for the dataset, an empty list should be returned.
```

2. Hypermedia pagination
```
Replicate code from the previous task.

Implement a get_hyper method that takes the same arguments (and defaults) as get_page and returns a dictionary containing the following key-value pairs:

    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer

Make sure to reuse get_page in your implementation.

You can use the math module if necessary.
```

3. Deletion-resilient hypermedia pagination
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.Start 3-hypermedia_del_pagination.py with this code
```
#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            pass
```
Implement a get_hyper_index method with two integer arguments: index with a None default value and page_size with default value of 10.
The method should return a dictionary with the following key-value pairs:
```

    index: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
    next_index: the next index to query with. That should be the index of the first item after the last item on the current page.
    page_size: the current page size
    data: the actual page of the dataset
```
Requirements/Behavior:
```
    Use assert to verify that index is in a valid range.
    If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
    If they request the next index (10) with page_size 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.
```
