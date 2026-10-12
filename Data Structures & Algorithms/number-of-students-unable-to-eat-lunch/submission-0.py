class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        q = deque(students)

        res = n
        for sandwich in sandwiches:
            cnt = 0
            while cnt < n and q[0] != sandwich:
                curr = q.popleft()
                q.append(curr)
                cnt += 1
            
            if q[0] == sandwich:
                q.popleft()
                res -= 1
            else:
                break
        return res
