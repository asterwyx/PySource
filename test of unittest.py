import unittest
from mydict_test import Mydict
class TestMydict(unittest.TestCase):
    
    def setUp(self):
        print('setUp...')
    
    def tearDown(self):
        print('tearDown...')

    def test_init(self):
        d = Mydict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
    
    def test_key(self):
        d = Mydict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Mydict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Mydict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Mydict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
        unittest.main()