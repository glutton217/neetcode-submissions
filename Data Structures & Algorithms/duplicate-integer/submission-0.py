class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map=dict()
        for num in nums:
            if my_map.get(str(num))==None:
                my_map[str(num)]=1
            else:
                return True
        return False