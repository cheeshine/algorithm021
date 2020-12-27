学习笔记

##### 深度优先搜索代码

```python
def nfs(node):
    if node is visited:
        # already visited
        return
        
    visited.add(node)
    
    # process current node
    # ... # logic here
    dfs(node.left)
    dfs(node.right)
```

##### dfs递归写法

```python
visited = set()

def nfs(node):
    if node is visited:  # terminator
        # already visited
        return
        
    visited.add(node)
    
    # process current node here
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

##### dfs非递归写法

```python
def dfs(self, tree):
    if tree.root is None:
        return []
        
    visited, stack = [], [tree.root]
    
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)
        
    # other processing work
    ...
```

##### bfs代码

```python
def bfs(graph, start, end):
    queue = []
    queue.apppend([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
    # other processing work
    ...
```

153

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]
```
