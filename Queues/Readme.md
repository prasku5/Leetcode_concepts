
# Python Queues and Heaps 🛠️

**Author**: Prasanna Kumar

---

## Introduction 📝

Queues and heaps are fundamental data structures that are widely used in programming. A queue is used to manage data in a first-in, first-out (FIFO) manner, while a heap is a specialized tree-based data structure used for efficient retrieval of the minimum or maximum element. Below is a detailed overview of both data structures, their variants, operations, and applications.

| **Data Structure** | **Explanation**                                                                                                 | **Operations**                        | **Time Complexity**                  | **Space Complexity**   | **Use Cases**                                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|---------------------------------------|--------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| **Queue**          | A linear data structure that follows the FIFO (First-In-First-Out) principle.                                  | Enqueue, Dequeue, Front, Rear        | O(1) for each operation              | O(n)                    | Scheduling tasks, managing resources, implementing breadth-first search (BFS), print queue, job scheduling.                                    |
| **Priority Queue** | A queue where each element is assigned a priority, and elements are dequeued based on their priority rather than their insertion order. | Insert, Remove, Peek                  | O(log n) for insert/remove           | O(n)                    | Scheduling tasks with priorities, Dijkstra's algorithm for shortest path, A* search, real-time systems.                                        |
| **Circular Queue** | A queue where the last position is connected back to the first position, creating a circular structure.       | Enqueue, Dequeue, Front, Rear        | O(1) for each operation              | O(n)                    | Buffer management, circular buffers, handling continuous data streams.                                                                         |
| **Deque**          | A double-ended queue that allows inserting and removing elements from both ends.                              | Append, Pop, AppendLeft, PopLeft      | O(1) for each operation              | O(n)                    | Sliding window algorithms, deque-based scheduling, palindromes, dynamic programming.                                                           |
| **Heap (Min/Max)** | A binary tree-based data structure used to efficiently get the smallest or largest element in constant time.   | Insert, RemoveMin/RemoveMax, Peek     | O(log n) for insert/remove           | O(n)                    | Efficient priority queues, heap sort, graph algorithms (Dijkstra, Prim), order statistics.                                                      |

---

## Types of Queues 🚪

### 1. **Queue (FIFO)**

A Queue follows the First-In-First-Out (FIFO) principle. The element that is added first will be removed first.

#### Operations:
- **Enqueue**: Add an element to the rear of the queue.
- **Dequeue**: Remove an element from the front of the queue.
- **Front**: Get the element at the front of the queue without removing it.
- **Rear**: Get the element at the rear of the queue without removing it.

#### Example:

```python
from collections import deque

queue = deque()
queue.append(10)  # Enqueue 10
queue.append(20)  # Enqueue 20
queue.append(30)  # Enqueue 30

print(queue.popleft())  # Dequeue (10)
print(queue[0])         # Front (20)
```

---

### 2. **Priority Queue (Min/Max)**

A priority queue stores elements with an associated priority. Elements with higher priority are dequeued first.

#### Operations:
- **Insert**: Add an element to the queue with a given priority.
- **RemoveMin/RemoveMax**: Remove the element with the highest (or lowest) priority.
- **Peek**: Get the element with the highest (or lowest) priority without removing it.

#### Example:

```python
import heapq

# Min-Heap example (default priority queue)
pq = []
heapq.heappush(pq, (1, "Task 1"))  # Insert with priority 1
heapq.heappush(pq, (3, "Task 3"))  # Insert with priority 3
heapq.heappush(pq, (2, "Task 2"))  # Insert with priority 2

# Remove element with the highest priority (lowest number)
print(heapq.heappop(pq))  # (1, "Task 1")
```

---

### 3. **Circular Queue**

A circular queue is a queue in which the last position is connected to the first position to form a circle. It is particularly useful for scenarios with fixed-size buffers.

#### Operations:
- **Enqueue**: Add an element to the queue.
- **Dequeue**: Remove an element from the queue.
- **Front**: Get the front element.
- **Rear**: Get the rear element.

#### Example:

```python
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full!")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.queue[self.front]

# Example usage
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.dequeue()
print(cq.peek())
```

---

### 4. **Deque (Double-Ended Queue)**

A Deque allows elements to be added and removed from both ends. It supports fast O(1) operations at both ends.

#### Operations:
- **Append**: Add an element to the rear.
- **Pop**: Remove an element from the rear.
- **AppendLeft**: Add an element to the front.
- **PopLeft**: Remove an element from the front.

#### Example:

```python
from collections import deque

dq = deque()
dq.append(10)
dq.append(20)
dq.appendleft(5)  # Add to the front
dq.pop()          # Remove from the rear
dq.popleft()      # Remove from the front
print(dq)
```

---

## Heaps 🌳

### 1. **Min-Heap**

A Min-Heap is a binary tree where the value of each node is smaller than or equal to the values of its children. The root node always contains the smallest value.

#### Operations:
- **Insert**: Add an element to the heap.
- **RemoveMin**: Remove the smallest element (root).
- **Peek**: Get the smallest element without removing it.

#### Example:

```python
import heapq

# Min-Heap example
min_heap = []
heapq.heappush(min_heap, 20)
heapq.heappush(min_heap, 15)
heapq.heappush(min_heap, 30)

print(heapq.heappop(min_heap))  # Removes and returns the smallest element (15)
print(min_heap)  # [20, 30]
```

---

### 2. **Max-Heap**

A Max-Heap is a binary tree where the value of each node is greater than or equal to the values of its children. The root node always contains the largest value.

#### Operations:
- **Insert**: Add an element to the heap.
- **RemoveMax**: Remove the largest element (root).
- **Peek**: Get the largest element without removing it.

#### Example:

```python
import heapq

# Max-Heap implementation (invert values to simulate max-heap)
max_heap = []
heapq.heappush(max_heap, -20)
heapq.heappush(max_heap, -15)
heapq.heappush(max_heap, -30)

print(-heapq.heappop(max_heap))  # Removes and returns the largest element (30)
print(max_heap)  # [-20, -15]
```

---

## Advanced Uses and Tips 💡

### 1. **Heap Sort**

HeapSort is an efficient sorting algorithm that uses a heap to sort elements.

```python
import heapq

def heap_sort(arr):
    heapq.heapify(arr)  # Convert array to heap
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_arr

arr = [10, 30, 20, 40, 50]
sorted_arr = heap_sort(arr)
print(sorted_arr)  # [10, 20, 30, 40, 50]
```

### 2. **Priority Queue with Custom Priorities**

You can use tuples to implement custom priority queues, where the first element is the priority.

```python
import heapq

pq = []
heapq.heappush(pq, (2, "low priority"))
heapq.heappush(pq, (1, "high priority"))
heapq.heappush(pq, (3, "medium priority"))

while pq:
    print(heapq.heappop(pq)[1])  # Prints elements in priority order
```

---

## Conclusion 🎯

- **Queues**: Useful for scenarios like task scheduling, buffering, and graph traversal.
- **Priority Queues**: Great for managing tasks with different priorities, commonly used in algorithms like Dijkstra’s.
- **Heaps**: Efficient for tasks requiring quick access to the minimum or maximum element, such as priority queues and heap sort.

---
