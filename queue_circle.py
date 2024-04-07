class Queue_circle:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")

            return
        
        print("Inserting:", item)
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1

        return item
    
    def is_empty(self):
        if self.size == 0:
            return True
        
        return False
    
    def is_full(self):
        if self.size == self.max_size:
            return True
        
        return False
    


if __name__ == "__main__":
    q = Queue_circle(3)
    q.enqueue("Tahmid")
    q.enqueue("Rafi")
    q.enqueue("Shawon")
    q.enqueue("Sakib")

    while not q.is_empty():
        person = q.dequeue()
        print("Removing:", person)

    q.enqueue("Sakib")
    print(q.items)
    print("Head: ", q.head)
    print("Tail: ", q.tail)
    print("Size: ", q.size)