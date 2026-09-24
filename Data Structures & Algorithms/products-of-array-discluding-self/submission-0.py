class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_array = []
        right_array =[]
        product=1
        for i in range(len(nums)):
            if i >0:
                product *=nums[i-1]
            left_array.append(product)
        right_product =1 
        for j in range(len(nums)-1,-1,-1):
            if j < len(nums)-1:
                right_product *= nums[j+1]
            right_array.append(right_product)
        right_array = right_array[::-1]
        

        result = []
        for k in range(len(nums)):
            result.append(left_array[k]*right_array[k])

        return result
