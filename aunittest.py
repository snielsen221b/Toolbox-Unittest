import unittest


class TestSortMethod(unittest.TestCase):
    def setUp(self):
        self.a_list = List([4, 7, 5, 6])

    def test_sorted(self):
        self.a_list.sort()
        sorted_list = a_list.get_list()
        for i in range(len(sorted_list)-1):
            self.assertTrue(sorted_list[i] <= sorted_list[i+1])

    def test_positive(self):
        self.a_list.remove_neg()
        pos_list = self.a_list.get_list()
        for x in pos_list:
            self.assertTrue(x >= 0)

    def test_pos_sort(self):
        self.a_list.pos_sort()
        pos_sorted = self.a_list.get_list()
        for i, x in enumerate(pos_sorted):
            if i < len(pos_sorted)-1:
                self.assertTrue(x >= 0)
                self.assertTrue(pos_sorted[i] <= pos_sorted[i+1])
            else:
                self.assertTrue(x >= 0)

    def tearDown(self):
        self.a_list.dispose()


class List(list):
    def __init__(self, list):
        self.list = list

    def get_list(self):
        return self.list

    def sort(self):
        for i in range(len(self.list)):
            for j in range(len(self.list)-1):
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]

    def remove_neg(self):
        for x in self.list:
            if x < 0:
                self.list.remove(x)

    def pos_sort(self):
        self.remove_neg()
        self.sort()


if __name__ == '__main__':
    unittest.main()
