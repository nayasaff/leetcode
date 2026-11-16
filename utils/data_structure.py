import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def __init__(self):
        self.queue = []
    
    def add(self, item, ascending= True):

        queue = self.queue
            
        # Handle empty queue case
        if not queue:
            queue.append(item)
            return
        insert_at = 0
        while insert_at < len(self.queue) and self.queue[insert_at] < item:
            insert_at += 1
        
        # Insert the item
        queue.insert(insert_at, item)
    
    def dequeue(self):
        
        return self.queue.pop()
    
    def dequeue_first_element(self) :
        return self.queue.pop(0)
    
    def __len__(self):
        return len(self.heap)