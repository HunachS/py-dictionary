class Dictionary:

    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]

    def hash(self, key: object) -> int:
        return hash(key) % self.size

    def __setitem__(self, key: object, value: object) -> None:
        index = self.hash(key)
        for ind, (k, v) in enumerate(self.hash_table[index]):
            if key == k:
                self.hash_table[index][ind] = (key, value)
                return
        self.hash_table[index].append((key, value))

    def __getitem__(self, key: object) -> object:
        index = self.hash(key)
        for k, v in self.hash_table[index]:
            if key == k:
                return v
        raise KeyError(key)

    def __len__(self) -> int:
        count = 0
        for buket in self.hash_table:
            count += len(buket)
        return count

    def loader_factory(self) -> None:
        loader_factory = len(self) / len(self.hash_table)
        if loader_factory > 0.7:
            self.re_hashing()

    def re_hashing(self) -> None:
        new_table = [[] for _ in range(self.size * 2)]
        old_table = self.hash_table
        self.hash_table = new_table
        for bucket in old_table:
            for k, v in bucket:
                self.__setitem__(k, v)
