import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        sor = []
        final = []
        done = []
        for i in points:
            dis = math.sqrt(((i[0]**2) + (i[1]**2)))
            arr.append(dis)
        for i, val in enumerate(arr):
            sor.append((val, i))
        sor.sort()
        for i in range(0, k):
            final.append(sor[i])
        for i in final:
            done.append(points[i[1]])
        return done
