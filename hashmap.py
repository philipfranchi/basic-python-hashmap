import logging
from decimal import Decimal

class HashMap:
    INITIAL_STORE_SIZE = 16
    LOAD_FACTOR = 0.5 


    def __init__(self):
        self.count = 0
        self.store = [ None ] * HashMap.INITIAL_STORE_SIZE
        

    def __getitem__(self, key):
        index = self._compute_index(key)
        if self.store[index] is not None and self.store[index][0] == key:
            return self.store[index][1]

        return None


    def  __setitem__(self, key, value):
        if self._should_resize_store():
            self._resize_store()
            
        index = self._compute_index(key)
        if self.store[index] is None:
            self.count += 1
        self.store[index] = (key, value)
            

    def __delitem__(self, key):
        index = self._compute_index(key)

        if self.store[index] is not None and self.store[index][0] == key:
            self.store[index] = None
            self.count -= 1
        else: 
            raise KeyError("No such key in map")


    def __contains__(self, key):
        return True if self.__getitem__(key) else False


    def __len__(self):
        return self.count


    def keys(self):
        keys = []
        for node in self.store:
            if node is not None:
                key, _ = node
                keys.append(key)
        return keys


    def _should_resize_store(self):
        current_load_factor = Decimal(self.count) / Decimal(len(self.store))
        if current_load_factor > HashMap.LOAD_FACTOR:
            return True
        return False

    def _resize_store(self):
        logging.debug("Resizing store")
        old_store = self.store
        self.store = [ None ] * (2 * len(old_store)) 
        self.count = 0

        for element in old_store:
            if element is not None:
                key, value = element
                self.__setitem__(key, value)


    def _compute_index(self, key):
        key_hash = hash(key)
        count = 0
        while count < len(self.store):
            index = (key_hash + (2 ** count) - 1) % len(self.store)
            if self.store[index] == None or self.store[index][0] == key:
                return index
            
            count += 1

        # This error should be unreachable. The quadratic probe 
        # will always have enough space when load factor is 1/2
        raise KeyError("Can't find index for item")
