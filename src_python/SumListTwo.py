class Solution:
    def SumListTwo(self,nums, target):
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return [dict[target-nums[i]],i]
            
obj = Solution()
nums=[2, 7, 11, 2, 7,15]
target=9
res=obj.SumListTwo(nums,target)
print(res)

dict = {}
for key,value in enumerate(nums):
    compliment=target-value
    if compliment not in dict:
        dict[value]=key
    else:
        print(dict[compliment],key)
