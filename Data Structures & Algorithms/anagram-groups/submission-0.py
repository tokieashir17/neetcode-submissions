class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for i in strs:
            S = ''.join(sorted(i))
            hashmap[S].append(i)
        return list(hashmap.values())
        
