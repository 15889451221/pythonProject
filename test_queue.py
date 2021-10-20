# class Queueq:
#     def __init__(self, capacity: int) -> None:
#         self.n = capacity
#         self.items = [-1]*capacity
#         self.head = 0
#         self.tail = 0
#
#     def enqueue(self, data):
#         if self.n == self.tail:
#             if self.head == 0:
#                 return False
#             for i in range(self.head, self.tail):
#                 self.items[i-self.head] = self.items[i]
#             self.tail -= self.head
#             self.head = 0
#         self.items[self.tail] = data
#         self.tail += 1
#         return True
#
#     def dequeue(self):
#         if self.head == self.tail:
#             return None
#         value = self.items[self.head]
#         self.head+=1
#         return value
#
#
# def test_queue():
#     a = Queueq()
#     a.enqueue("10")
#     a.enqueue("20")
#     a.enqueue("30")
#     deque_item = a.dequeue()
#     assert deque_item == "10"
#     assert a.head.data == "20"
#     assert a.head.next.data == "30"
#
#
# if __name__ == "__main__":
#     test_queue()