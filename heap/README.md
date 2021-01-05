
# Heap / Priority Queue
[Python3 공식 문서 (Heap)](https://docs.python.org/3/library/heapq.html)    
[Python3 공식 문서 (Priority Queue)](https://docs.python.org/ko/3/library/asyncio-queue.html#priority-queue)

## 1. Heap
### ```heapq``` 모듈 사용. list를 heap으로 사용할 수 있게 해줌.      *단, Min-Heap이니 주의할 것*
```python3
import heapq
myHeap = []
```    

### Heap - 주요 Methods

* #### ```heappush(heap, item)``` - heap에 삽입(minHeap)
```python3
heapq.heappush(myHeap, 5)
heapq.heappush(myHeap, 1)
heapq.heappush(myHeap, 3)
# myHeap = [1, 5, 3]
```
* #### ```pop(heap)``` - Root의 값(min)을 pop
```python3
heapq.pop(myHeap) # 1, myHeap = [3, 5]
heapq.pop(myHeap) # 3, myHeap = [5]
```

* #### ```heappushpop(heap, item)``` - 개별 heappush + pop 보다 더 빠름!

* #### ```heapify(myList)``` - List를 heap의 형태를 만족하도록 변환.


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
- [x] [더 맵게] https://programmers.co.kr/learn/courses/30/lessons/42626
- [ ] [디스크 컨트롤러] https://programmers.co.kr/learn/courses/30/lessons/42627
- [ ] [이중우선순위큐] https://programmers.co.kr/learn/courses/30/lessons/42628
