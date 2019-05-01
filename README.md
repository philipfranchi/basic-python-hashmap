# HashMap implementation in Python
This is a basic Hash Map implementation in Python, using only native python libraries.
To use it, simply import the class like so
`from hashmap import HashMap`.
The class offers the following functions:
- `__setitem__` in O(1) time, accessed with square brackets e.g: `hash_map["key"] = value`.
- `__getitem__` in O(1) time, accessed with square brackets e.g: `hash_map["key"]`. Returns `None` if the key is not in the Map.
- `__delitem__`, in O(1) time, accessed with the `del` keyword e.g : `del hash_map["key"]`. Throws a `KeyError` if the key is not in the Map.
- `keys`, which returns a list of keys in O(n) time, where n is the number of items in the list: `hash_map.keys()`.
- `__contains__`, in O(1) time, returns a boolean indicating if the key is in the Map: `value in hash_map`.


I've also included a few unit tests for this class, which helped me during development. To run them on your machine, just run the file in your terminal: `python test_hashmap.py`