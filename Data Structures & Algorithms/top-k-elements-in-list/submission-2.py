class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: return [x for x, _ in __import__('collections').Counter(nums).most_common(k)]