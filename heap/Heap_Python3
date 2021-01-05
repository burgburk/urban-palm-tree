# Heap (in Python3)
파이썬 공식 문서 : https://docs.python.org/3/library/heapq.html
### Python3 : ```heapq``` 모듈 사용. list를 heap으로 사용할 수 있게 해줌.

```python3
import heapq
myHeap = []
```

### ```heappush(heap, item)``` - heap에 삽입(minHeap)
```python3
heapq.heappush(myHeap, 5)
heapq.heappush(myHeap, 1)
heapq.heappush(myHeap, 3)
# myHeap = [1, 5, 3]
```
### ```pop(heap)``` - Top(min)을 pop
```python3
heapq.pop(myHeap) # 1, myHeap = [3, 5]
heapq.pop(myHeap) # 3, myHeap = [5]
```

```heappushpop(heap, item)``` - 개별 heappush + pop 보다 더 빠름!
### List를 Heap으로 변환 - ```heapify(myList)```

```heapq.nlargest(N, iterable, key = None)``` - Return a list with the _n_ largest elements from the dataset defined by _iterable_. _key_, if provided, specifies a function of one argument that is used to extract a comparison key from each element in _iterable_ (for example, `key=str.lower`). Equivalent to: `sorted(iterable,  key=key,  reverse=True)[:n]`.
