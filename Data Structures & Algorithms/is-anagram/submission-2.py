class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map=dict()
        for letter in s:
            if (my_map.get(letter)==None):
                my_map[letter]=1
            else:
                my_map[letter]+=1
        for letter in t:
            if (my_map.get(letter)==None):
                return False
            else:
                my_map[letter]-=1
        for key,value in my_map.items():
            if value!=0:
                return False
        return True