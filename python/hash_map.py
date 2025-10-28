class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.map = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.map[index]
        for (k, v) in bucket:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        bucket = self.map[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.map):
            print(f"Bucket {i}: {bucket}")

if __name__ == "__main__":
    h = HashMap()
    h.put("apple", 10)
    h.put("banana", 20)
    h.put("orange", 30)
    print("banana =", h.get("banana"))
    print("apple =", h.get("apple"))
    h.put("banana", 50)
    print("updated banana =", h.get("banana"))
    h.remove("orange")
    print("After removing 'orange':")
    h.display()
