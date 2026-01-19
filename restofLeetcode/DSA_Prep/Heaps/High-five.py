"""
This problem is just about using heaps to solve the top k scores for students. This probme is all about knowhing your heaps
"""


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        answer = []
        if not items:
            return answer


        hm = {}
        import heapq

        for stu,score in items:
            #we are going to check to see if student is in set if they are we will add to hashmap if not then we will create heap and add it to hashmap with score. At the end we will pop the top 5 scores per student and then calculate the average and then replace the heap in the hashmap

            #first check to see if hashmap
            if stu not in hm:
                ll = [score*-1]
                heapq.heapify(ll)
                hm[stu] = ll
            elif stu in hm:
                heapq.heappush(hm[stu],(score*-1))

        for stu,heap in hm.items():
            avg = 0
            count = 1
            while heap and count <= 5:
                hh = heapq.heappop(heap)*-1
                avg+=hh
                count+=1
            answer.append([stu,avg//5])
        answer = sorted(answer,key=lambda x: x[0])
        return answer