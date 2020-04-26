---
title: Word break
tags: [dynamic-programming, string, level-4]
---

# {{title}}

:fa fa-tag fa-fw: [dynamic-programming]({{tagspath}}/dynamic-programming)
:fa fa-tag fa-fw: [string]({{tagspath}}/string)
:fa fa-tag fa-fw: [level-4]({{tagspath}}/level-4)

Practice Link: [LeetCode](https://leetcode.com/problems/word-break/)

Description:

- Given a non-empty string `s` and a dictionary `wordDict` containing a list of non-empty words, determine if `s` can be segmented into a space-separated sequence of one or more dictionary words.

Example 1:

```text
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
```

Example 2:

```text
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
```

Example 3:

```text
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
```

Note:

- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/dp/word-break.py ':include :type=code')
<!-- tabs:end -->