import heapq

def solution(scoville, K):
    i = 0
    heapq.heapify(scoville)
    m1 = heapq.heappop(scoville)
    while m1 < K:
        if not scoville:
            return -1
        m2 = heapq.heappop(scoville)
        heapq.heappush(scoville, m1 + 2 * m2)
        i += 1
        m1 = heapq.heappop(scoville)
    return i


"""
heapq 라이브러리를 이용하는 것이 훨씬 직관적이고 효율성 측면에서 뛰어나다는 것을 확인할 수 있었다.
다른 문제들도 파이썬에서 제공하는 라이브러리들을 이용하여 푸는 것으로 전략을 잡아야 할 듯 하다.
"""

if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))
