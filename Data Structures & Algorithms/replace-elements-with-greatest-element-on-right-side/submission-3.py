class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp = []
        for num in arr:
            tmp.append(num)
        for i in range(len(arr)-1):
            tmp.remove(arr[i])
            arr[i] = max(tmp)
        arr[len(arr)-1] = -1
        return arr