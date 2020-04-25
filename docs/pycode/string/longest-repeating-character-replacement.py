import collections


class Solution(object):
    def characterReplacement(self, s, k):
        count = collections.Counter()
        start = result = 0
        for end in range(len(s)):
            count[s[end]] += 1
            max_count = count.most_common(1)[0][1]
            if end - start + 1 - max_count > k:
                count[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
        return result