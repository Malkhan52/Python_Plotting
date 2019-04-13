def _testQ1(n, s, k, b):
    return int(compute_size_of_dense_unclustered_index(n, s, k, b))

def testQ1():
    # n = 10, s = 8, k = 4, b = 20
    assert _testQ1(10, 8, 4, 20) == 2, "Not correct."
    
    # n = 100, s = 8, k = 4, b = 50
    assert _testQ1(100, 8, 4, 50) == 8, "Not correct."

    # n = 100, s = 8, k = 4, b = 49
    assert _testQ1(100, 8, 4, 49) == 9, "Not correct."

    # n = 100, s = 8, k = 6, b = 49
    assert _testQ1(100, 8, 6, 49) == 13, "Not correct."
    
    # n = 10, s = 12, k = 4, b = 20
    assert _testQ1(10, 12, 4, 20) == 2, "Not correct."
    
    print("Q1 PASS.")

def _testQ2(n, s, k, b):
    #print(int(compute_size_of_sparse_clustered_index(n, s, k, b)))
    return int(compute_size_of_sparse_clustered_index(n, s, k, b))

def testQ2():
    # n = 10, s = 8, k = 4, b = 20
    assert _testQ2(10, 8, 4, 20) == 1, "Not correct."
    
    # n = 100, s = 8, k = 4, b = 50
    assert _testQ2(100, 8, 4, 50) == 2, "Not correct."

    # n = 100, s = 8, k = 4, b = 49
    assert _testQ2(100, 8, 4, 49) == 2, "Not correct."

    # n = 100, s = 8, k = 6, b = 49
    assert _testQ2(100, 8, 6, 49) == 3, "Not correct."
    
    # n = 10, s = 12, k = 4, b = 20
    assert _testQ2(10, 12, 4, 20) == 2, "Not correct."
    
    print("Q2 PASS.")

def testQ3_1():
    btree = BTree([19],
              [BTree([7, 13],
                     [BTree([3, 5], ["3", "5"]),
                      BTree([7, 11], ["7", "11"]),
                      BTree([13, 17], ["13", "17"])
                     ]),
               BTree([29],
                     [BTree([29], ["29"])])
              ],
              n = 2, d = 1)
    catched = False
    try:
        btree._check_block_usage_between_half_and_full()
    except AssertionError:
        catched = True
    if not catched:
        raise Exception("_check_block_usage_between_half_and_full() failed to detect errors.")
    
def testQ3():
    testQ3_1()
    print("Q3 PASS.")
    
def testQ4_1():
    btree = BTree([19, 31],
              [BTree([7, 13],
                     [BTree([3, 5], ["3", "5"]),
                      BTree([7, 11], ["7", "11"]),
                      BTree([13, 17], ["13", "17"])
                     ]),
               BTree([23],
                     [BTree([19], ["19"]),
                      BTree([23], ["23"])
                     ]),
               BTree([37], ["37"])
              ],
              n = 2, d = 1)
    catched = False
    try:
        btree.check(is_root = True)
    except AssertionError:
        catched = True
    if not catched:
        raise Exception("_check_is_balanced() failed to detect errors.")

def testQ4():
    testQ4_1()
    print("Q4 PASS.")

        
        
def testQ5_1():
    btree = BTree([19],
              [BTree([7, 13],
                     [BTree([3, 5], ["3", "5"]),
                      BTree([7, 11], ["7", "11"]),
                      BTree([13, 17], ["13", "17"])
                     ]),
               BTree([29, 31],
                     [BTree([19], ["19"]),
                      BTree([29], ["29"]),
                      BTree([31, 37], ["31", "37"])
                     ])
              ],
              n = 2, d = 1)
    assert btree.lookup(20) == None, "Found unexpected key 20"
    assert btree.lookup(37) == '37', "Key 37 not found in B-Tree"

    
def testQ5():
    testQ5_1()
    print("Q5 PASS.")

def _testQ7(num = 10):    
    ht = ChainedHashTable(b = 10, k = 3)
    ht.h = lambda x: h(x, ht.b)
    all = list(range(num))
    import random
    random.shuffle(all)
    for x in all:
        ht.insert((x, str(x)))
    #ht.show()
    myans = {}
    for i in range(10):
        bucket = ht.table[i]
        ret = get_all_from_bucket(bucket)
        ret.sort()
        #print(ret)
        keys = [x[0] for x in ret]
        if keys == []: continue
        myans[i] = keys
    return myans


def testQ7():
    ans = {}
    ans[10] = {0:[0], 1:[1, 9], 4:[2, 8], 5:[5], 6:[4, 6], 9:[3,7]}
    assert _testQ7(10) == ans[10], "Error in random insert 0 - 9"
    print("Q7 PASS.")    

def get_all_items(table):
    ret = []
    for w in table:
        ret.append(get_all_from_bucket(w))
    return ret

def testQ8_1():
    ht = ExtensibleHashTable(k = 4, bucket_size = 2)
    ht.insert((1, str(1)))
    ht.insert((3, str(3)))
    ht.insert((5, str(5)))
    ht.insert((7, str(7)))
    ans = [[(1, '1'), (3, '3')], [(5, '5'), (7, '7')], [], []]
    cur = get_all_items(ht.table)
    assert(cur == ans), "Check failed after 4 inserts."
    ht.insert((2, str(2)))
    ht.insert((4, str(4)))
    ans = [[(1, '1')], [(3, '3'), (2, '2')], [(5, '5'), (4, '4')], [(7, '7')], [], [], [], []]
    cur = get_all_items(ht.table)
    assert(cur == ans), "Check failed after 6 inserts."

def testQ8():
    testQ8_1()
    print("Q8 PASS.")
    pass
