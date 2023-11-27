import unittest

def merge(left, right):
    list_merge = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list_merge.append(left[i])
            i += 1
        else:
            list_merge.append(right[j])
            j += 1
    list_merge += left[i:]
    list_merge += right[j:]
    return list_merge


def sort(seq: list) -> list:
    if len(seq) <= 1:
        return seq
    middle = len(seq) // 2
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)

class TestSorted(unittest.TestCase):
    def test_void_list(self):
        self.assertListEqual([], sort([]))

    def test_unit_list(self):
        self.assertListEqual([1,2], sort([2,1]))

    def test_unsorted_list(self):
        self.assertListEqual([1,2,4,7,8,10,14,16], sort([10,7,14,16,2,8,4,1]))

if __name__ == '__main__':
    unittest.main()