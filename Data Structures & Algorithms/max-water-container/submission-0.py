class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        store = 0
        while L < R:
            area = (R-L)*(min(heights[R], heights[L]))
            store = max(area, store)
            if heights[L] < heights[R]:
                L += 1
            elif heights[L] > heights[R]:
                R -= 1
            elif heights[L] == heights[R]:
                L += 1

        return store

        