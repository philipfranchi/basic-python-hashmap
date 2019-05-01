import unittest, logging
from hashmap import HashMap


class MapTest(unittest.TestCase):

    def test_can_get_value_from_map(self):
        m = HashMap()
        m["key"] = "value"
        self.assertEqual("value",  m["key"] )
        self.assertTrue("key" in m)
        self.assertEqual(1, len(m))


    def test_get_from_map_when_key_does_not_exist_returns_None(self):
         m = HashMap()
         value = m["key"]
         self.assertIsNone(value)


    def test_can_delete_value_from_map(self):
        m = HashMap()
        m["key"] = "value"
        del m["key"]
        self.assertFalse("key" in m)
        self.assertEqual(0, len(m))


    def test_that_delete_when_key_does_not_exist_throws_error(self):
        m = HashMap()
        self.assertRaises(KeyError, m.__delitem__, "key")
    

    def test_set_item_does_not_incriment_count_when_a_value_already_exists(self):
        m = HashMap()
        m["key"] = "value"
        self.assertEqual(1, len(m))

        m["key"] = "new value"
        self.assertEqual(1, len(m))


    def test_store_properly_resizes_when_space_is_exceeded(self):
        m = HashMap()
        size = 32
        expected_store_size = size * 2
        for i in range(size):
            m[i] = i
        
        self.assertEqual(size, len(m))
        self.assertEqual(expected_store_size, len(m.store))


    def test_keys_correctly_returns_set_of_keys_in_map(self):
        m = HashMap()
        size = 32
        for i in range(size):
            m[i] = i

        keys = m.keys()
        self.assertEqual(size, len(keys))
        for i in range(size):
            self.assertTrue(i in keys)


    def test_keys_returns_empty_list_when_the_map_is_empty(self):
        m = HashMap()
        self.assertEqual(0, len(m))
        keys = m.keys()
        self.assertEqual([], keys)

if __name__ == '__main__':
    unittest.main()