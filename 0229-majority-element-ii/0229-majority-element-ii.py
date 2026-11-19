class Solution(object):
    def majorityElement(self, nums):

        candidate1 = None
        candidate2 = None

        count1 = 0
        count2 = 0

        for i in nums:
            
            if i == candidate1:
                count1 += 1

            elif i == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = i
                count1 = 1

            elif count2 == 0:
                candidate2 = i
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        result = []

        for i in [candidate1, candidate2]:
            if i is not None and nums.count(i) > len(nums) // 3:
                if i not in result:
                    result.append(i)

        return result