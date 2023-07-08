import types

def flat_generator(list_of_lists):
    flat_list = []
    def recursion_to_flat_list(input_list):
        try:
            for el in input_list:
                if not isinstance(el,list):
                    flat_list.append(el)
                else:
                    recursion_to_flat_list(el)
        except Exception as e:
            print(repr(e))
    recursion_to_flat_list(list_of_lists)
    for i in flat_list:
        yield i
  



def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()


