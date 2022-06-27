class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = {}
        # res = []
        count = 0

        # loop over list, for each num, add to hashmap
        # hashmap key = num, value = list of index
        # at each one, if there is a pair existing, for each elm in the values, that is one pair

        for i,num in enumerate(nums):
            if hashmap.get(num,None) != None:
                for pair in hashmap[num]:
                    # res.append([pair,i])
                    count += 1
                hashmap[num].append(i)
            else:
                hashmap[num]=[i]

        # print("res",res)
        return count