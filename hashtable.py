

# Declare the empty hash table and fill with 40 empty lists.
# This constructor is called from routes.py, trucks.py, and packages.py.
class HashTable:
    def __init__(self, initial_capacity):
        self.initial_capacity = initial_capacity
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert key-value pairs into the hash table. This method is called from packages.py and routes.py.
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Search for duplicate keys, and replace duplicate values instead of double-adding.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search the hash table by key and return the associated value. This method is called from dijkstra.py.
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
        return None

    # Make the hash table instances subscriptable for easier searching and printing
    def __getitem__(self, key):
        value = self.search(key)
        return value

    # Delete key-value pairs from the hash table.
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
