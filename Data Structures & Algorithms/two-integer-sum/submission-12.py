class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map=defaultdict(list)
        for index, number in enumerate(nums):
            if my_map.get(str(number))!=None:
                my_map[str(number)].append(index)
            else:
                my_map[str(number)].append(index)
        for number in nums:
            if my_map.get(str(target-number))!=None:
                if number==target-number:
                    if len(my_map.get(str(number)))>1:
                        return [my_map.get(str(number))[0], my_map.get(str(target-number))[1]]
                    continue
                else:
                    return [my_map.get(str(number))[0], my_map.get(str(target-number))[0]]