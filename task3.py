class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []
        
    def __iter__(self):
        self.count = -1
        self.recursion_to_flat_list(self.list_of_list)
        return self

    def __next__(self):
        self.count += 1
        if self.count < len(self.flat_list):
            return self.flat_list[self.count]
        else:
            raise StopIteration
        
    def recursion_to_flat_list(self,input_list):
        try:
            for el in input_list:
                if not isinstance(el,list):
                    self.flat_list.append(el)
                else:
                    self.recursion_to_flat_list(el)
        except Exception as e:
            print(repr(e))





def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
