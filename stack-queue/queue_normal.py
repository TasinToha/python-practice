class Queue_normal:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def is_empty(self):
        if self.items == []:
            return True
        return False
    

if __name__ == "__main__":
    q = Queue_normal()
    q.enqueue("Tahmid")
    q.enqueue("Rafi")
    q.enqueue("Shawon")

    while not q.is_empty():
        item = q.dequeue()
        print(item)