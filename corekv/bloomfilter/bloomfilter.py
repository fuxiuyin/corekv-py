import math


class BloomFilter:
    def __init__(self, max_item_count: int, fpr: float) -> None:
        self.max_item_count = max_item_count
        self._hash_func = hash

        self._m = math.ceil(self._calculate_m(fpr) / 8) * 8
        self._round = self._calculate_k_num()

        self._bitmap = bytearray(self._m // 8)
        
    def _calculate_m(self, fpr: float) -> None:
        m = -self.max_item_count * math.log(fpr) / 0.4804530139182014
        return math.ceil(m / 8) * 8
    
    def _calculate_k_num(self):
        return math.ceil(
            0.6931471805599453 * (self._m / self.max_item_count)
        )
    
    def may_has(self, key):
        for _ in range(self._round):
            key = self._hash_func(key)
            tkey = key % self._m
            if (self._bitmap[tkey // 8] & (1 << (tkey % 8))) == 0:
                return False
        return True
    
    def insert(self, key):        
        for _ in range(self._round):
            key = self._hash_func(key)
            tkey = key % self._m
            self._bitmap[tkey // 8] |= 1 << (tkey % 8)
