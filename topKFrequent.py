# https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent1(nums: list[int], k: int) -> list[int]:
    freq = dict()
    for n in nums:
        if n not in freq:
            freq[n] = 1
        else:
            freq[n] += 1
    sorted_dict = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    res = [x for (x, y) in sorted_dict[0:k]]

    return res


def topKFrequent2(nums: list[int], k: int):
    freq = {}
    bucket = [[] for x in range(len(nums) + 1)]

    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    for key, val in freq.items():
        bucket[val].append(key)

    res = []
    for i in range(len(bucket) - 1, 0, -1):
        for b in bucket[i]:
            res.append(b)
            if len(res) == k:
                return res


nums = [3, 3, 2, 3, 1, 2, 3, 2, 4]
k = 2
# res = topKFrequent(nums, k)
res = topKFrequentOptimal(nums, k)
print(res)
