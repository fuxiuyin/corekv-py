import string
import random

from skiplist import SkipList


test_str_length = 21

def random_str():
    return (''.join([random.choice(string.ascii_letters + string.digits)
                     for _ in range(test_str_length)]))



def test_skip_list_basic_crud():
    key_count = 1000000
    skip_list = SkipList()
    for i in range(key_count):
        key = "key-%d" % i
        value = "value-%d" % i
        skip_list.set(key, value)
        
    for i in range(key_count):
        key = "key-%d" % i
        expected_value = "value-%d" % i
        value = skip_list.get(key)
        assert value == expected_value, \
               "expected %s for key %s, but got %s" % (expected_value,
                                                       key, value)
    
    del_list = set()
    for i in range(key_count // 2):
        random_int = random.randint(0, key_count)
        key = "key-%d" % random_int
        del_list.add(random_int)
        skip_list.remove(key)
    
    for i in range(key_count):
        key = "key-%d" % i
        value = skip_list.get(key)
        if i in del_list:
            expected_value = None
        else:
            expected_value = "value-%d" % i
        assert value == expected_value, \
               "expected %s for key %s, but got %s" % (expected_value,
                                                       key, value)


def test_draw_list():    
    skip_list = SkipList()
    key_count = 90
    for i in range(key_count):
        key = "%d" % i
        value = "%d" % i
        skip_list.set(key, value)
    skip_list.draw(1)    


if __name__ == "__main__":
    # test_skip_list_basic_crud()
    test_draw_list()