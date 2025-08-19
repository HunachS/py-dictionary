class Dictionary:

    def __init__(self, size: int = 8) -> None:
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
        self.length = 0

    def hash(self, key: object) -> int:
        return hash(key) % self.size

    def __setitem__(self, key: object, value: object) -> None:
        index = self.hash(key)
        for ind, (k, v) in enumerate(self.hash_table[index]):
            if key == k:
                self.hash_table[index][ind] = (key, value)
                return
        # додаємо новий ключ
        self.length += 1
        self.hash_table[index].append((key, value))
        # перевірка load factor
        self.loader_factory()

    def __getitem__(self, key: object) -> object:
        index = self.hash(key)
        for k, v in self.hash_table[index]:
            if key == k:
                return v
        raise KeyError(key)

    def __len__(self) -> int:
        return self.length

    def loader_factory(self) -> None:
        load_factor = self.length / self.size
        if load_factor > 0.7:
            self.re_hashing()

    def re_hashing(self) -> None:
        old_table = self.hash_table
        self.size *= 2  # збільшуємо розмір
        self.hash_table = [[] for _ in range(self.size)]
        self.length = 0  # скидаємо лічильник і перерахуємо його правильно

        for bucket in old_table:
            for k, v in bucket:
                self.__setitem__(k, v)  # додаємо заново
