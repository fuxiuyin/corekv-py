import string
import random

from bloomfilter import BloomFilter


test_str_length = 32

def random_str():
    return (''.join([random.choice(string.ascii_letters + string.digits)
                     for _ in range(test_str_length)]))
    

def test_bloom_filter():
    inserted_strs = set([random_str() for _ in range(5000)])
    for fpr in [0.1, 0.2, 0.3, 0.4, 0.5]:
        bloom_filter = BloomFilter(5000, fpr)
        for s in inserted_strs:
            bloom_filter.insert(s)
            
        for s in inserted_strs:
            assert bloom_filter.may_has(s) == True, "key miss %s" % s
        
        fp_count = 0
        test_count = 1000000
        for _ in range(test_count):
            s = random_str()
            while s in set():
                s = random_str()
            if bloom_filter.may_has(s):
                fp_count += 1
        tfpr = fp_count / test_count
        print("m: %d, k: %d expected fpr: %f true fpr %f" % (
            bloom_filter._m, bloom_filter._round, fpr, tfpr)
        )
        assert fpr - 0.1 < tfpr < fpr + 0.1, \
            "expected fpr: %f true fpr %f" % (fpr, tfpr)


if __name__ == "__main__":
    test_bloom_filter()
