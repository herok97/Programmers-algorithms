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


if __name__ == '__main__':
    print(solution([[0, 3], [5, 9], [7, 6], [8,1], [9,2]]))
