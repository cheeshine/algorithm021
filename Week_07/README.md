学习笔记

```python
class Trie(object): 
	def __init__(self):
		self.root = {}
		self.end_of_word = "#"  	

	def insert(self, word):
		node = self.root
		for char in word:
			node = node.setdefault(char, {})
		node[self.end_of_word] = self.end_of_word

	def search(self, word):
		node = self.root
		for char in word:
			if char not in node:
				return False
			node = node[char]
		return self.end_of_word in node  	
	def startsWith(self, prefix):
		node = self.root
		for char in prefix:
			if char not in node:				
				return False
			node = node[char]
		return True
```

```python
def TwoEndedBFS(graph, start, end):
    lqueue=collections.deque()
    rqueue=collections.deque()

    lqueue.append(beginWord)
    rqueue.append(endWord)

    lvisited.add(beginWord)
    rvisited.add(endWord)
    step=0

    while lqueue and rqueue:
        if len(lqueue)>len(rqueue):
            lqueue,rqueue=rqueue,lqueue
            lvisited,rvisited=rvisited,lvisited
            step+=1
            for k in range(len(lqueue)):
                node=lqueue.popleft()
                if node in rvisited:
                    return step
				
                process(node)
                nodes = generate_related_nodes(node)
                lqueue.append(nodes)
                lvisited.add(nodes)
```

