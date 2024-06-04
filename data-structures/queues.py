from collections import deque
import time
import threading

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        return self.buffer
        
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]
    
    

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})
print(pq.size())
print(pq.dequeue())
print(pq.dequeue())


orders = ['pizza','samosa','pasta','biryani','burger']

############ Exercise One ###########
print("")
print("############ Answers to Exercise One ################")
print("")  

def place_order(orders):
    for order in orders:
        print(sqs.enqueue(order))
        time.sleep(0.5)
        
def serve_order():
    time.sleep(1)
    while sqs.buffer:
        print(sqs.dequeue())
        time.sleep(2)
   
sqs = Queue()
        
t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
t2.start()

t1.join()
t2.join()

############ Exercise Two ###########
print("")
print("############ Answers to Exercise Two ################")
print("")  

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print(front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


produce_binary_numbers(10)