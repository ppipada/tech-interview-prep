---
title: Rotate image
tags: [array, level-3]
---

# {{title}}

:fa fa-tag fa-fw: [array]({{tagspath}}/array)
:fa fa-tag fa-fw: [level-3]({{tagspath}}/level-3)

Practice Link: [LeetCode](https://leetcode.com/problems/rotate-image/)

Description:

- You are given an n x n 2D matrix representing an image.
- Rotate the image by 90 degrees (clockwise).

Example 1:

```text
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```

Example 2:

```text
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

Note:

- You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
- DO NOT allocate another 2D matrix and do the rotation.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/array/rotate-image.py ':include :type=code')
<!-- tabs:end -->