from __future__ import annotations
from DataStructure.Heap.MinHeap import MinHeap

from InformationRetrieval.Query.QueryResultItem import QueryResultItem


class QueryResult:

    __items: [QueryResultItem]

    def __init__(self):
        self.__items = []

    def add(self, docId: int, score: float = 0.0):
        self.__items.append(QueryResultItem(docId, score))

    def size(self) -> int:
        return len(self.__items)

    def getItems(self) -> [QueryResultItem]:
        return self.__items

    def intersection(self, queryResult: QueryResult) -> QueryResult:
        result = QueryResult()
        i = 0
        j = 0
        while i < self.size() and j < queryResult.size():
            item1 = self.__items[i]
            item2 = queryResult.__items[j]
            if item1.getDocId() == item2.getDocId():
                result.add(item1.getDocId())
                i = i + 1
                j = j + 1
            else:
                if item1.getDocId() < item2.getDocId():
                    i = i + 1
                else:
                    j = j + 1
        return result

    def getBest(self, K: int):
        minHeap = MinHeap(2 * K, lambda x1, x2: -1 if x1.getScore() > x2.getScore() else (0 if x1.getScore() == x2.getScore() else 1))
        for queryResultItem in self.__items:
            minHeap.insert(queryResultItem)
        self.__items.clear()
        i = 0
        while i < K and not minHeap.isEmpty():
            self.__items.append(minHeap.delete())
            i = i + 1

    def __repr__(self):
        return f"{self.__items}"
