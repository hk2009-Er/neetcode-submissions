class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        st=set()
        i=0
        while i < len(nums) - 2:
            j= i+1
            k=len(nums)-1
            while j < k:
                if nums[j] + nums[i] + nums[k] ==0:
                    st.add((nums[i], nums[j], nums[k]))
                    j +=1
                    k -=1
                elif (nums[j] + nums[i] + nums[k]) < 0:
                    j +=1
                elif (nums[j] + nums[i] + nums[k]) > 0:
                    k -=1
            i  +=1
        result = list(st)
        result = [list(x) for x in st]
        return result
        
