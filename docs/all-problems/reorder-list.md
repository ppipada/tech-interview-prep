---
title: Reorder list
tags: [linkedlist, 'level-3']
---

# {{title}}

{{#tags}}
:fa fa-tag fa-fw: [{{.}}]({{tagspath}}/{{.}})
{{/tags}}
{{^tags}}
:fa fa-tag fa-fw: "No tags found !!!"
{{/tags}}

Practice Link: [LeetCode](https://leetcode.com/problems/reorder-list/)

Description:

- Given a singly linked list `L: L0→L1→…→Ln-1→Ln`, reorder it to: `L0→Ln→L1→Ln-1→L2→Ln-2→…`
- You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

```text
Given 1->2->3->4, reorder it to 1->4->2->3.
```

Example 2:

```text
Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/linkedlist/reorder-list.py ':include :type=code')
<!-- tabs:end -->
