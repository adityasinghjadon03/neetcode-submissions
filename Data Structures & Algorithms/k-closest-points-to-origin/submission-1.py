# import math

# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         arr = []
#         sor = []
#         final = []
#         done = []
#         for i in points:
#             dis = math.sqrt(((i[0]**2) + (i[1]**2)))
#             arr.append(dis)
#         for i, val in enumerate(arr):
#             sor.append((val, i))
#         sor.sort()
#         for i in range(0, k):
#             final.append(sor[i])
#         for i in final:
#             done.append(points[i[1]])
#         return done

class Solution:
    def kClosest(self, points, k):
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        def partition(l, r):
            pivotIdx = r
            pivotDist = euclidean(points[pivotIdx])
            i = l
            for j in range(l, r):
                if euclidean(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        L, R = 0, len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        return points[:k]