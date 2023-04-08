from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self._index = 0
        self._data = data

    def __next__(self):
        try:
            item = self._data[self._index]
        except IndexError:
            raise StopIteration
        else:
            self._index += 1
            return item
