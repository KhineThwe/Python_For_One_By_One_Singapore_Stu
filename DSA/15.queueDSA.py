class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def check_empty(self):
        return len(self.queue) < 1

    def dequeue(self):
        if self.check_empty():
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.display()
    q.dequeue()

    print("After removing an element: ")
    q.display()

