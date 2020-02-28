"""
(value, ref-next) ==> SinglelyLL
(ref-prev, value, ref-next) == DLL
slots (linked list) ==> []*3
cache {} ==> {key, values}
input format = (key, value)
input((1, 0)) [(1, 0)]
input((2, 4)) [(2, 4),(1, 0)]
input((3, 6)) [(3, 6), (2, 4), (1, 0)]
input((5, 9)) [(5, 9), (3, 6), (2, 4)] --1
input((2, 2)) [(2, 2), (5, 9), (3, 6)]

///
arrA = [1, 3, 4, 7]
arrA[2] = 4
for i in range(len(arrA)):
    arrA[i]

node1<==>node2<==>node3
node1.next = node2
"""
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # state the limit of node the lru cache can hold
        self.limit = limit
        # create a linked list to hold the key value pair
        self.storageList = DoublyLinkedList()
        # track the current number of node it is holding
        self.currentNode = 0
        # create a storage dict for fast acccess to node in the cache
        self.cacheStorage = {}


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # if the key does not exist in the cache_storage return None
        if key not in self.cacheStorage:
            return None
        # otherwise return the value associated with the key and move its node to the head of the storage List
        else:
            """
            {key: (ref-prev, value=(key, item), ref-next)}
            self.cacheStorage[key] = (ref-prev, value, ref-next)
            """
            node = self.cacheStorage[key]
            self.storageList.move_to_front(node)       
            return node.value[1]


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # if the key exist in the cache storage, replace its value and move the node to the head in the storage list
        if key in self.cacheStorage:
            # get node stored in dictionary with key ref
            node = self.cacheStorage[key]
            # update/overwrite the value of the node stored in the dictionary
            node.value = (key, value)
            self.storageList.move_to_front(node)
        else:
        # check if the length of the node is up to the limit
            if self.currentNode == self.limit:
        #if it is, delete the tail of the cache_list and remove the key value pair from the cache_storage
        # delete item from dictionary
                del self.cacheStorage[self.storageList.tail.value[0]]
                # delete node from DLL
                self.storageList.remove_from_tail()
        # add the new key value pair to the cache_storage and cache_list head
                node = self.storageList.add_to_head((key, value))
                self.cacheStorage[key] = self.storageList.head
        # if the length is not up to the limit, simply add the new key value pair to the cache_storage and cache_list head and increment node_count
            else:
                node = self.storageList.add_to_head((key,value))
                self.cacheStorage[key] = self.storageList.head
                self.currentNode += 1
