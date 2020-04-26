---
title: Decode ways
tags: [string, dynamic-programming, level-4]
---

# {{title}}

:fa fa-tag fa-fw: [string]({{tagspath}}/string)
:fa fa-tag fa-fw: [dynamic-programming]({{tagspath}}/dynamic-programming)
:fa fa-tag fa-fw: [level-4]({{tagspath}}/level-4)

Practice Link: [LeetCode](https://leetcode.com/problems/decode-ways/)

Description:

- A message containing letters from A-Z is being encoded to numbers using the following mapping:

    ```text
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    ```

- Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

```text
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
```

Example 2:

```text
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/string/decode-ways.py ':include :type=code')
<!-- tabs:end -->