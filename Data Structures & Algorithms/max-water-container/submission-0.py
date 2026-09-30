class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        i=0
        j=len(heights)-1
        while i < j:
            height = min(heights[i], heights[j] )
            width = j - i
            area = height * width
            max_water = max(max_water,area)

            if heights[i] < heights[j]:
                i +=1
            else:
                j -=1
        return max_water
