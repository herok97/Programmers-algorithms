def solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = []
    # 다리를 지나지 않은 트럭 또는 지나고 있는 트럭이 존재하면
    while len(truck_weights) > 0 or len(bridge) > 0:
        # 다리를 지나는 차 전진
        for truck in bridge:
            truck[1] += 1

        # 차 퇴장
        for i, truck in enumerate(bridge):
            if truck[1] > bridge_length:
                bridge.pop(i)

        # 차 입장
        total_weights = sum([w[0] for w in bridge])
        if len(truck_weights) > 0 and (len(bridge) == 0 or total_weights + truck_weights[0] <= weight):
            bridge.append([truck_weights.pop(0), 1])
        cnt += 1
    return cnt


# 출처: https://programmers.co.kr/learn/courses/30/lessons/42583/solution_groups?language=python3 김형준님 외 3명
import collections
DUMMY_TRUCK = 0
class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def best_solution1(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


# 출처: https://programmers.co.kr/learn/courses/30/lessons/42583/solution_groups?language=python3 심명훈님 외 241명
def best_solution2(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec



def modified_solution(bridge_length, weight, truck_weights):
    cnt = 0
    bridge = []
    # 다리를 지나지 않은 트럭 또는 지나고 있는 트럭이 존재하면
    while len(truck_weights) > 0 or bridge:
        # 다리를 지나는 차 전진
        for truck in bridge:
            truck[1] += 1

        # 차 퇴장
        for i, truck in enumerate(bridge):
            if truck[1] > bridge_length:
                bridge.pop(i)

        # 차 입장
        total_weights = sum([w[0] for w in bridge])
        if truck_weights and (len(bridge) == 0 or total_weights + truck_weights[0] <= weight):
            bridge.append([truck_weights.pop(0), 1])
        cnt += 1
    return cnt

'''
두 번쨰 클래스를 이용한 풀이는 속도가 본인의 코드보다 2~4배 정도 빨랐다. 그 부분을 분석해보면 좋을 것 같다.
세 번째 풀이는 본인의 코드보다 최대 30배까지 느렸다. 간단해보여서 좋은 것 같은데 왜이렇게 느린지 판단해보면 좋을 것 같다.
추가로 list를 조건문에 이용하는 것을 볼 수 있었는데 빈 리스트면 False 그렇지 않으면 True를 출력한다고 한다.
마지막으로 본인의 코드를 수정하여 작성해놓았다.
'''
if __name__ == '__main__':
    solution(100, 100, [10,10,10,10,10,10,10,10,10,10])
    pass
