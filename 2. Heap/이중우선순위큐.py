def solution(operations):
    queue = []
    for com in operations:
        if 'I' in com:
            n = int(com.split(' ')[-1])
            insert(queue, n)
        elif 'D 1' in com:
            try:
                queue.pop(0)
            except IndexError:
                pass
        elif 'D -1' in com:
            try:
                queue.pop(-1)
            except IndexError:
                pass
        else:
            pass
    try:
        answer = [queue[0], queue[-1]]
    except IndexError:
        answer = [0, 0]
    return answer

def insert(queue, n):
    i = 0
    while queue and queue[i] >= n:
        i += 1
        if i >= len(queue):
            break
    try:
        queue.insert(i, n)
    except IndexError:
        queue.append(n)


"""
마땅한 best case가 없어서 다음과 같이 본인 코드만 작성
"""

if __name__ == '__main__':
    print(solution(["I 7","I 5","I -5","D -1"]))
