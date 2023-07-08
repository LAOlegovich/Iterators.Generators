class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []
        
    def __iter__(self):
        self.count = -1
        #self.flat_list = [el for i in self.list_of_list for el in i]
        for i in self.list_of_list:
            for el in i:
                self.flat_list.append(el)
        return self

    def __next__(self):
        self.count += 1
        if self.count < len(self.flat_list):
            return self.flat_list[self.count]
        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

