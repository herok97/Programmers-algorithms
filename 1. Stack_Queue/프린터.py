def my_solution(priorities, location):
    a = [0] * 100
    a[:len(priorities)] = priorities[:]

    begin = 0
    end = len(priorities) - 1
    cnt = 0

    while True:
        if begin < end:
            if a[begin] < max(a[begin:end]):
                end += 1
                end = end % 100
                a[end] = a[begin]
                if begin == location:
                    location = end
            else:
                cnt += 1
                if begin == location:
                    return cnt
            begin += 1
            begin = begin % 100
        else:
            if a[begin] < max(a[begin:] + a[:end]):
                end += 1
                end = end % 100
                a[end] = a[begin]
                if begin == location:
                    location = end
            else:
                cnt += 1
                if begin == location:
                    return cnt
            begin += 1
            begin = begin % 100


def best_solution(priorities, location):
    # 출처: https://programmers.co.kr/learn/courses/30/lessons/42587/solution_groups?language=python3 김소영님 외 42명
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


"""

본인의 코드는 최대한 append 연산을 사용하지 않으려고 하다보니 복잡해졌다. 미리 리스트를 선언하고(100개가 최대라고 했기 때문에)
순환 리스트 큐 구조를 생각했는데, 오히려 max 연산에서 시간을 많이 잡아먹는 듯 했다.
또한, 리스트의 처음과 끝을 begin, end로 정의하고 그 사이를 큐라고 생각했는데, begin과 end의 순서가 뒤바뀌었을 때 list에 접근하는 것을
고려해야 했기 때문에 코드가 길어졌다.

아래 best_solution에서는 queue를 list + tuple 형태로 구현하였고 (통상 이렇게 하는듯) pop 함수와 any 함수를 잘 이용했다.
any 함수는 처음 보는건데 좋은 것 같다. 또한 append 연산을 수행했는데 생각보다 연산 속도가 빨라서 놀랐다.

"""

if __name__ == '__main__':
    pass
