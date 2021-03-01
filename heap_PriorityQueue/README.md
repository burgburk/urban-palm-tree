

# Heap / Priority Queue
[Python3 공식 문서 (Heap)](https://docs.python.org/3/library/heapq.html)    
[Python3 공식 문서 (Priority Queue)](https://docs.python.org/ko/3/library/asyncio-queue.html#priority-queue)     
    
## 1. Heap
### ```heapq``` 모듈 사용. list를 heap으로 사용할 수 있게 해줌.      *Min-Heap으로 구현*
```python3
import heapq
myHeap = []
```    

* #### ```heapq.heappush(heap, item)``` - Push the value item onto the heap, maintaining the heap invariant.
```python3
heapq.heappush(myHeap, 5)
heapq.heappush(myHeap, 1)
heapq.heappush(myHeap, 3)
# myHeap = [1, 5, 3]
```    
* #### ```heapq.heappop(heap)``` - Pop and return the smallest item from the heap, maintaining the heap invariant. If the heap is empty, IndexError is raised. To access the smallest item without popping it, use heap[0].
```python3
heapq.heappop(myHeap) # 1, myHeap = [3, 5]
heapq.heappop(myHeap) # 3, myHeap = [5]
```    

* #### ```heappushpop(heap, item)``` - Push item on the heap, then pop and return the smallest item from the heap. The combined action runs more efficiently than heappush() followed by a separate call to heappop().

* #### ```heapify(myList)``` - Transform list x into a heap, in-place, in linear time.
```python3
arr = [5,4,3,2,1]
heapq.heapify(arr)

# arr = [1,2,3,5,4]
```

* #### ```heapq.nlargest(N, iterable, key = None) / heapq.n(smallest(...)``` - Return a list with the _n_ largest elements from the dataset defined by _iterable_. _key_, if provided, specifies a function of one argument that is used to extract a comparison key from each element in _iterable_ (for example, `key=str.lower`). Equivalent to: `sorted(iterable,  key=key,  reverse=True)[:n]`.    
    
## 2. Priority Queue
### ```PriorityQueue``` 모듈 사용 (```queue``` 내장 모듈에서 제공, heapq로 구현됨)
```python3
from queue import PriorityQueue
myPQ = PriorityQueue()

# Queue Size 조정 가능(Default는 무한대)
myPQ = PriorityQueue(maxsize=10)
```    
* #### ```put(item)``` - PQ에 삽입
```python3
myPQ.put(4)
myPQ.put(1)
myPQ.put(3)
```    
* #### ```get()``` - 우선순위에 따라 item 삭제 후 return
```python3
print(que.get()) # 1
print(que.get()) # 3
print(que.get()) # 4
```    
* #### 정렬 기준 변경 - (key, value)의 tuple형태로 ```put/get```
```python3
myPQ.put((3, 'Apple'))
myPQ.put((1, 'Banana'))
myPQ.put((2, 'Cherry'))

print(myPQ.get()[1])  # Banana
print(myPQ.get()[1])  # Cherry
print(myPQ.get()[1])  # Apple
```    



    
## Problems
- [x] [\[더 맵게\]](https://prorammers.co.kr/learn/courses/30/lessons/42626) - 프로그래머스 lv2
- [ ] [\[디스크 컨트롤러\]](https://programmers.co.kr/learn/courses/30/lessons/42627) - 프로그래머스 lv3
- [ ] [\[이중우선순위큐\]](https://programmers.co.kr/learn/courses/30/lessons/42628) - 프로그래머스 lv3 
- [ ] [\[최대 힙\]](https://www.acmicpc.net/problem/11279) / [\[최소 힙\]](https://www.acmicpc.net/problem/1927) / [\[절댓값 힙\]](https://www.acmicpc.net/problem/11286)- 백준 실버 1, 2
- [ ] [\[\[가운데를 말해요\]\]](https://www.acmicpc.net/problem/1655) - 백준 골드 2     

* [백준 우선순위 큐 문제 모음](https://www.acmicpc.net/problemset?sort=ac_desc&algo=59)
