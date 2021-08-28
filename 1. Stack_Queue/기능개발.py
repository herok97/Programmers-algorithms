def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:
        # Speeds 만큼 Progresses 진행
        for i in range(len(speeds)):
            progresses[i] += speeds[i]

        cnt = 0
        # 첫 번째 기능이 완료된 경우 연속된 완료된 기능들 배포 & count
        while len(progresses) > 0 and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        # 배포된 기능의 수 저장
        if cnt != 0:
            answer.append(cnt)

    return answer

def best_solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p - 100) // s):
            Q.append([-((p - 100) // s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


"""
본인의 코드는 문제를 그대로 해석하여 풀었다. 매 시간마다 progress에 speeds를 더해 업데이트하며, 동시에 제일 먼저 진행되어야
하는 첫 번째 기능이 완료되었는지 확인한다. 첫 번째 기능의 완료가 확인된 경우 첫 번째 기능을 포함한 연속된 기능들을 배포한다.

아래 best_solution에서는 수식적인 표현이 많이 들어가서 직관적이지 못하다. 본인이 느끼기엔 best는 아닌 것 같지만
많은 사람들이 선택한 방법이다.

"""

if __name__ == '__main__':
    solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
