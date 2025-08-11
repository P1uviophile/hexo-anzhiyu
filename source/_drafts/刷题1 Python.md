---
title: 刷题记录 （python练习?

author: Joking

tags:

- 二叉?
- Python

cover: https://pic.joking7.com/202407042121281.webp

date: 2025-07-02 21:01:00

categories:

- leetcode
---


Python 真难写啊

## 7.2

### [199. 二叉树的右视?- 力扣（LeetCode）](https://leetcode.cn/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=top-interview-150)

广度优先 层序遍历后每层取最右边的结点储?

时间复杂??遍历所有子节点 O(N)

空间复杂??最坏情况下包含一层的所有节点O(n/2)；最好情况下（链表树）只包含一个节点O(1)

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            res.append(q[0].val)
            for _ in range(n):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
        return res

```

深度优先 优先遍历右子?

时间复杂??遍历所有子节点 O(N)

空间复杂??最坏情况下（链表树）包含所有节点O(n)；最好情况下只包含一个节点O(1)

```python
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        self.max_depth = -1
        res = []

        def dfs(root: Optional[TreeNode], depth):
            if depth > self.max_depth:
                self.max_depth += 1
                res.append(root.val)
            if root.right :
                dps(root.right,depth+1)
            if root.left :
                dps(root.left,depth+1)
        
        dps(root,0)
        return res
```



### [637. 二叉树的层平均?- 力扣（LeetCode）](https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150)

层序遍历每层相加取平均?

时间复杂??遍历所有子节点 O(N)

空间复杂??最坏情况下包含一层的所有节点O(n/2)；最好情况下（链表树）只包含一个节点O(1)

```python
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []
        q = deque([root])
        res = []
        while q:
            n = len(q)
            sum = 0.0
            for _ in range(n):
                node = q.popleft()
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
                sum += node.val
            res.append(sum/n)
        return res

```



### [103. 二叉树的锯齿形层序遍?- 力扣（LeetCode）](https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150)

想得太多?同样层序遍历最后看flag反转list就行

```python
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = deque([root])
        res = []
        flag = -1
        while q:
            n = len(q)
            list = []
            for _ in range(n):
                node = q.popleft()
                list.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if flag == 1:
                list.reverse()
            flag *= -1
            res.append(list)
        return res
```



### [112. 路径总和 - 力扣（LeetCode）](https://leetcode.cn/problems/path-sum/?envType=study-plan-v2&envId=top-interview-150)

Pycharm的调试功能挺好用?

深度优先遍历，判断是否叶子节?

```python
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None : return False
        def dfs(root:Optional[TreeNode],sum,targetSum):
            if root.left is None and root.right is None:
                if sum+root.val == targetSum : return True
                return False
            if root.left :
                if dfs(root.left,sum+root.val,targetSum):
                    return True
            if root.right :
                if dfs(root.right,sum+root.val,targetSum):
                    return True
            return False
        return dfs(root,0,targetSum)
```



### [114. 二叉树展开为链?- 力扣（LeetCode）](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/?envType=study-plan-v2&envId=top-interview-150)

递归 左右子树拼接 这样空间复杂度为O(1)

```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None: return

        def dfs(root: Optional[TreeNode], lastNode: Optional[TreeNode]) -> TreeNode:
            if root.left is None and root.right is None: return root
            if root.left:
                lastNode = dps(root.left, lastNode)
            if lastNode is not None:
                lastNode.right = root.right
                root.right = root.left
                root.left = None
                if lastNode.right:
                    lastNode = dfs(lastNode.right, None)
            else :
                if root.right:
                    lastNode = dfs(root.right, None)
            return lastNode

        dfs(root, None)

```



## 7.3

### [173. 二叉搜索树迭代器 - 力扣（LeetCode）](https://leetcode.cn/problems/binary-search-tree-iterator/description/?envType=study-plan-v2&envId=top-interview-150)

很容易想到的是先遍历得到中序遍历存储起来,然后一个个访问,不过空间复杂度是O(N)

```python
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.p = deque()
        self.dfs(root)

    def next(self) -> int:
        return self.p.popleft()

    def hasNext(self) -> bool:
        return len(self.p) != 0

    def dfs(self,root):
        if root is None:
            return
        self.dfs(root.left)
        self.p.append(root.val)
        self.dfs(root.right)
```

不容易想到的解法是维护一个栈使其存储根节点到当前节点的一条链,空间复杂度为O(H), H为树的高?均摊时间复杂度为O(1)

这里next压入栈不用递归 和初始化一个原?

```python
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.p = deque()
        node = root
        while node:
            self.p.append(node)
            node = node.left

    def next(self) -> int:
        node = self.p.pop()
        res = node.val
        cur = node.right
        while cur:
            self.p.append(cur)
            cur = cur.left
        return res

    def hasNext(self) -> bool:
        return len(self.p) != 0
```



### [117. 填充每个节点的下一个右侧节点指?II - 力扣（LeetCode）](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150)

容易想到的是层次遍历挨个连接节点,空间复杂度O(N)

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None: return root
        q = deque()
        q.append(root)
        while q:
            cur = Node(0)
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                cur.next = node
                cur = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            cur.next = None
        return root
```

不容易想到的是利用每一层的头节点用next遍历每层,因为next实际上已经为我们将每层连接成链表?所以不用额外空?空间复杂度O(1)

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur=root
        while cur:
            ans=dummy=Node()
            while cur:
                if cur.left:
                    ans.next=cur.left
                    ans=ans.next
                if cur.right:
                    ans.next=cur.right
                    ans=cur.right
                cur=cur.next
            cur=dummy.next
        return root
```

碰到个bug 力扣给的Node的构造函数是这样的：

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
```

实际写到Pycharm里面的时候self.next被调用的时候如果next为None会导致指向next函数生成的某个对象而不是None 需要改成None



### [129. 求根节点到叶节点数字之和 - 力扣（LeetCode）](https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/?envType=study-plan-v2&envId=top-interview-150)

最大难点是我搞不懂Python的全局变量怎么?

```python
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        global s
        s = 0
        def dfs(root: Optional[TreeNode],last):
            global s
            if root.left is None and root.right is None:
                s += last * 10 + root.val
            if root.left:  dfs(root.left, last*10+root.val)
            if root.right:  dfs(root.right, last * 10 + root.val)

        dfs(root,0)
        return s
```



## 7.4

### [236. 二叉树的最近公共祖?- 力扣（LeetCode）](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150)

没想出来 解法有点天才

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None : return None
        if root.val == p.val or root.val == q.val: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None: return right
        if right is None: return left
        return root
```



### [222. 完全二叉树的节点个数 - 力扣（LeetCode）](https://leetcode.cn/problems/count-complete-tree-nodes/description/?envType=study-plan-v2&envId=top-interview-150)

简单写法就直接遍历得到节点个数,这样时间复杂度是O(N)

```Java
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null){ return 0; }
        return countNodes(root.left) + countNodes(root.right) + 1;
    }
}
```

把最底层看作数组，可以用二分的方法找到切割位置，不过代码好难写啊 时间复杂度是O(logN * logN)

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        if not root.left: return 1
        p = root
        depth = -1
        while p:
            depth += 1
            p = p.left
        left = 0
        right = 2 ** depth
        mid = right // 2
        while left < right:
            p = root
            num = bin(mid).replace('0b', '').rjust(depth,'0')
            for n in range(len(num)):
                if num[n] == '0':
                    p = p.left
                else:
                    p = p.right
            if p: left = mid+1
            if not p: right = mid
            mid = (left + right ) // 2
        res = 0
        for n in range(depth):
            res += 2 ** n
        res += left
        return res
```

看到大佬用递归拆分普通二叉树和完全二叉树?太强?

```python
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left, right = root, root
        ld, rd = 0, 0
        while left:
            ld += 1
            left = left.left
        while right:
            rd += 1
            right = right.right
        
        # 按照满二叉树计算
        if ld == rd:
            return pow(2, ld) - 1
        
        # 按照普通二叉树计算
        return  1+self.countNodes(root.left)+self.countNodes(root.right)
```

