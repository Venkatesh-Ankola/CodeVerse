class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        print(intervals)

        i =1
        while i < len(intervals):
            print(i)
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1],intervals[i][1])
                intervals.remove(intervals[i])
            else:
                i+=1

        return intervals
        