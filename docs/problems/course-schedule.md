---
title: Course schedule
tags: [graph]
---

# {{title}}

:fa fa-tag fa-fw: [graph]({{tagspath}}/graph)

Description:

- There are a total of numCourses courses you have to take, labeled from `0` to `numCourses-1`.
- Some courses may have prerequisites, for example to take course `0` you have to first take course `1`, which is expressed as a pair: `[0,1]`
- Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

```text
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
```

Example 2:

```text
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
```

Constraints:

- The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
- You may assume that there are no duplicate edges in the input prerequisites.
- 1 <= numCourses <= 10^5

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../../pycode/graph/course-schedule.py ':include :type=code')
<!-- tabs:end -->