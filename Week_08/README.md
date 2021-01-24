学习笔记

```python
def bubble_sort(alist):
    length = len(alist)
    for i in range(length - 1):
        # i表示比较多少轮
        for j in range(length - i - 1):
            # j表示每轮比较的元素的范围，因为每比较一轮就会排序好一个元素的位置，
            # 所以在下一轮比较的时候就少比较了一个元素，所以要减去i
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
```

```python
def selection_sort(alist):
    length = len(alist)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[i]:
                alist[j], alist[i] = alist[i], alist[j]
```

```python
def insert_sort(alist):
    for i in range(1, len(alist)):
        # 从第二个元素开始，每次取出一个元素，插入前面的序列使其有序
        for j in range(i, 0, -1):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
```

```python
def quick_sort(alist, start, end):
    if start >= end:
        return
    low = start
    high = end
    mid = alist[low]
    
    while low < high:
        while low < high and mid < alist[high]:
            # 从右边开始找，如果元素小于基准，则把这个元素放到左边
            high -= 1
        alist[low] = alist[high]
        
        while low < high and mid > alist[low]:
            # 从左边开始找，如果元素大于基准，则把元素放到右边
            low += 1
        alist[high] = alist[low]
    
    # 循环退出，low==high，把基准元素放到这个位置
    alist[low] = mid
    
    # 递归调用，重新排列左边的和右边的序列
    quick_sort(alist, start, low-1)
    quick_sort(alist, low+1, end)
```

```python
def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n / 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
        # 得到新的步长
        gap = gap / 2
```

```python
def merge_sort(alist):
    if len(alist) <= 1:
        return
    num = len(alist) / 2
    # 划分
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    # 合并
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.append(left[l:])
    result.append(right[r:])
    return result
```
