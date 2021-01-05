# Heap
파이썬 공식 문서 : https://docs.python.org/3/library/heapq.html
## Python3 : ```heapq``` 모듈 사용. list를 heap으로 사용할 수 있게 해줌.      단, Min-Heap이니 주의할 것

```python3
import heapq
myHeap = []
```   

## 주요 Methods

* ### ```heappush(heap, item)``` - heap에 삽입(minHeap)
```python3
heapq.heappush(myHeap, 5)
heapq.heappush(myHeap, 1)
heapq.heappush(myHeap, 3)
# myHeap = [1, 5, 3]
```
* ### ```pop(heap)``` - Top(min)을 pop
```python3
heapq.pop(myHeap) # 1, myHeap = [3, 5]
heapq.pop(myHeap) # 3, myHeap = [5]
```

* ### ```heappushpop(heap, item)``` - 개별 heappush + pop 보다 더 빠름!

* ### ```heapify(myList)``` - List를 heap의 형태를 만족하도록 변환.


* ```heapq.nlargest(N, iterable, key = None) / heapq.n(smallest(...)``` - Return a list with the _n_ largest elements from the dataset defined by _iterable_. _key_, if provided, specifies a function of one argument that is used to extract a comparison key from each element in _iterable_ (for example, `key=str.lower`). Equivalent to: `sorted(iterable,  key=key,  reverse=True)[:n]`.



## Problems
- [x] [더 맵게] https://programmers.co.kr/learn/courses/30/lessons/42626
- [ ] [디스크 컨트롤러] https://programmers.co.kr/learn/courses/30/lessons/42627
- [ ] [이중우선순위큐] https://programmers.co.kr/learn/courses/30/lessons/42628
