学习笔记

树的面试题一般都是递归
- 节点的定义
- 重复性（自相似性）


递归-循环
- 通过函数体来进行的循环

计算n！
```python
def Factorial(n):
    if n <= 1:
        return 1
    return n * Factorial(n - 1)
```

递归代码模板（==记忆==）
```python
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return
    
    # process logic in current level
    process(level, data, ...)
    
    # drill down
    self.recursion(level + 1, param1, ...)
    
    # reverse the current level status if needed
```

思维要点
1. 不要人肉进行递归（最大误区）
2. 找到最近最简方法，将其拆解成可重复解决的问题（重复子问题）
3. 数学归纳法思维

idea写出子函数名 然后自动生成函数体

分治代码模板
```python
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return
        
    # prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subreuslt3 = self.divide_conquer(subproblems[2], p1, ...)
    ...
    
    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
    
    # revert the current level status
```