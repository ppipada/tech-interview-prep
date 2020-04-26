---
title: Add and search word - data structure design
tags: [trie, backtracking, level-4]
---

# {{title}}

:fa fa-tag fa-fw: [trie]({{tagspath}}/trie)
:fa fa-tag fa-fw: [backtracking]({{tagspath}}/backtracking)
:fa fa-tag fa-fw: [level-4]({{tagspath}}/level-4)

Practice Link: [LeetCode](https://leetcode.com/problems/add-and-search-word-data-structure-design/)

Description:

- Design a data structure that supports the following two operations:

    ```text
    void addWord(word)
    bool search(word)
    ```

- Search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`.
- A `.`means it can represent any one letter.
- You may assume that all words are consist of lowercase letters `a-z`.

Example:

```text
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
```

Solution:

<!-- tabs:start -->
#### **Python**

[Python](../pycode/trie/add-and-search-word.py ':include :type=code')
<!-- tabs:end -->
