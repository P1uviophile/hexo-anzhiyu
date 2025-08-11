---
title: Debug 合集 1

author: Joking

tags:

- SQLite
- DEBUG

cover: https://pic.joking7.com/2024-11-19-00-47-23.webp

date: 2024-06-28 16:01:00

categories:

- 苦练
---
### Mybatis-Plus 的默认 Insert 方法不支持 SQLite 主键id自增后返回id

写毕设项目的时候遇到的 需要插入一条新的记录然后返回新记录的主键id 这个id是自增的

然后发现Mybatis-Plus的默认Insert方法不支持这个操作 可以插入但是不能返回自增后的id

后来用事务解决了：本来用SQLite就是考虑到项目的数据量较小才用的 所以直接用串行化在插入操作之后查询SELECT last_insert_rowid()获取刚刚插入的记录的id字段

上网查了一下似乎改一下sqlite-jdbc的版本就能解决？不过我没试过：[sqlite-jdbc版本导致插入数据自增id问题](https://www.cnblogs.com/qingzhen/p/17944868)

### CentOS SQLite临时文件溢出

![2024-11-20-00-03-17](https://pic.joking7.com/2024-11-20-00-03-17.webp)

明天着急检查 先用 rm -rf /tmp/sqlite-jdbc-tmp* 指令删了再说 之后再找溢出原因

### 力扣刷题bug

[117. 填充每个节点的下一个右侧节点指针 II - 力扣（LeetCode）](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150)

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

在Pycharm里写的时候self.next被调用的时候如果next为None会导致指向next函数生成的某个对象而不是None 需要改成None
