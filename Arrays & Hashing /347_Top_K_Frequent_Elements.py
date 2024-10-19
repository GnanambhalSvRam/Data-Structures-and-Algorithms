class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for num in nums:
            if num in hmap.keys():
                hmap[num] += 1
            else:
                hmap[num] = 1
        
        res = []
        sorted_dict = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
        print("sorted hashmap = ")
        print(sorted_dict)
        for i, (key,value) in enumerate(sorted_dict.items()):
            if i>=k:
                break
            res.append(key)

        return res
