import collections


class ListNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:

    # somthing is wrong
    def __init__(self):
        self.size = 100
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        head = self.table[index]

        if head.val is None:
            head.key = key
            head.val = value
            head.next = ListNode()
        else:
            while head.val is not None:
                if head.key == key:
                    # find key and update
                    head.val = value
                    break
                head = head.next

            head.key, head.val = key, value
            head.next = ListNode()

    def get(self, key: int) -> int:
        index = key % self.size
        head = self.table[index]

        ret_val = -1
        while head:
            if key == head.key:
                ret_val = head.val
                break
            head = head.next

        return ret_val

    def remove(self, key: int) -> None:
        index = key % self.size
        prev = head = self.table[index]

        while head:
            if key == head.key:
                prev = head.next
                break

            #update prev to head
            prev = head
            #udpate head
            head = head.next

        self.table[index] = prev


if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 10)
    obj.put(1, 15)
    obj.put(101, 100)
    obj.put(1001, 111)
    obj.put(5, 12)
    obj.put(10, 11)
    print(obj.get(1))
    print(obj.get(5))
    print(obj.get(101))
    print(obj.get(102))
    obj.remove(101)
    print(obj.get(101))
