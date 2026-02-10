from typing import List, Optional

class Heap:
    def __init__(self, data: Optional[List[int]] = None):
        self.items = data[:] if data is not None else []
        if self.items:
            self._build()

    def __len__(self) -> int:
        return len(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def to_list(self) -> List[int]:
        return self.items[:]

    def peek(self) -> int:
        if not self.items:
            raise IndexError("heap is empty")
        return self.items[0]

    def insert(self, value: int) -> None:
        self.items.append(value)
        self._sift_up(len(self.items) - 1)

    def extract_min(self) -> int:
        if not self.items:
            raise IndexError("heap is empty")
        min_val = self.items[0]
        last = self.items.pop()
        if self.items:
            self.items[0] = last
            self._sift_down(0)
        return min_val

    def _sift_up(self, i: int) -> None:
        while i > 0:
            parent = (i - 1) // 2
            if self.items[i] < self.items[parent]:
                self.items[i], self.items[parent] = self.items[parent], self.items[i]
                i = parent
            else:
                break

    def _sift_down(self, i: int) -> None:
        size = len(self.items)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < size and self.items[left] < self.items[smallest]:
                smallest = left
            if right < size and self.items[right] < self.items[smallest]:
                smallest = right
            if smallest == i:
                break
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            i = smallest

    def _build(self) -> None:
        for i in range(len(self.items) // 2 - 1, -1, -1):
            self._sift_down(i)