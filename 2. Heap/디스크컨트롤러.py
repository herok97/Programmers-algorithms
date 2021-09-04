import heapq

def solution(jobs):
    heapq.heapify(jobs)
    h = []
    t = 0
    n = len(jobs)
    sum_time = 0

    while jobs or h:
        while jobs and t >= jobs[0][0]:
            heapq.heappush(h, (jobs[0][1], jobs[0][0]))
            heapq.heappop(jobs)
        if h:
            working_time, input_time = heapq.heappop(h)
            t += working_time
            sum_time += t - input_time
        else:
            t += 1

    return sum_time // n

"""
본인의 코드는 jobs 라는 힙 구조와 task 라는 힙 구조를 가지고 있다. task 는 현재 처리하는(해야되는) 일들을 저장하고 있으며,
jobs 는 아직 요청이 들어오지 않은, 요청 될 일들을 저장하고 있다.
첫 번째 동작은 jobs 에서 현재 요청해야 하는 일들을 task 로 전달하는 것이다.
두 번째 동작은 task 에 일이 있을 경우 일을 처리하고 그만큼의 시간을 경과시키는 것이다 t += working_time
이 때, 처리할 일이 없으면 t += 1 하여 시간이 지나도록 한다.
특이사항은 위의 일들을 한 번에 처리한다는 것이다. 예를 들어 현재 일이 처리되어 t=10이 되었는데, jobs에 t<10 인 일들이 여러 개 있을 경우
한 번에 task 로 가져오게 된다. 또한, task 에 존재하는 일들도 한 번에 처리하고 t 를 갱신하게 된다.
"""

if __name__ == '__main__':
    print(solution([[0, 3], [5, 9], [7, 6], [8,1], [9,2]]))
