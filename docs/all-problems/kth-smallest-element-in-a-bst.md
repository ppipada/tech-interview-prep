---
title: Kth smallest element in a BST
tags: [tree, binary-search, level-3]
---

# {{title}}

:fa fa-tag fa-fw: [tree]({{tagspath}}/tree)
:fa fa-tag fa-fw: [binary-search]({{tagspath}}/binary-search)
:fa fa-tag fa-fw: [level-3]({{tagspath}}/level-3)

Practice Link: [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

Description:

- Given a binary search tree, write a function `kthSmallest` to find the `k`th smallest element in it.

Example 1:

```text
Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
```

Example 2:

```text
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
```

Note:

- You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:

- What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
- How would you optimize the kthSmallest routine?

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/tree/kth-smallest-element-in-a-bst.py ':include :type=code')
<!-- tabs:end -->