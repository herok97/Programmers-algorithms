# 정답 리스트를 최대한 static하게 선언하여 효율성 향상시킴
def modified_solution(prices):
    answer = [0] * len(prices)
    cur = 0
    while cur < len(prices):
        cnt = cur + 1
        while cnt < len(prices) - 1 and prices[cur] <= prices[cnt]:
            cnt += 1
        answer[cur] = (cnt - cur)
        cur += 1
    answer[-1] = 0
    return answer

# 정확도 테스트와 효율성 테스트 모두 통과한 코드, pop 연산을 제외하고 indexing을 활용하여 효율성 문제 해결
def my_solution(prices):
    answer = []
    cur = 0
    while cur < len(prices):
        cnt = cur + 1
        while cnt < len(prices) - 1 and prices[cur] <= prices[cnt]:
            cnt += 1
        answer.append(cnt - cur)
        cur += 1
    answer[-1] = 0
    return answer


# 본인이 작성한 코드로 정확도 테스트는 통과하였으나, 효율성 테스트에서 떨어진 코드
def bad_solution(prices):
    answer = []
    while prices:
        cnt = 1
        while cnt < len(prices) - 1 and prices[0] <= prices[cnt]:
            cnt += 1
        prices.pop(0)
        answer.append(cnt)

    answer[-1] = 0
    return answer


# 출처: https://programmers.co.kr/learn/courses/30/lessons/42584/solution_groups?language=python3 hwangda님 외 188 명
def best_solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

'''
best solution 에서 볼 수 있는 장점은 정답으로 제출될 배열을 미리 정적으로 선언해둔다는 점, 정답 배열에 직접 값을 더하여 추가적인 변수 생성을
하지 않았다는 점, for j in range(i+1, len(prices)) 구문을 이용해 마지막 배열의 값이 0이 되도록 했다는 점을 들 수 있다. 
또한, answer[i] +=1 break 구문이 아주 인상적이다.
break, continue, pass 등을 잘 활용하는 것도 코드를 깔끔하게 만들 수 있는 방법인 것 같다.
'''

if __name__ == '__main__':
    my_solution([1, 2, 3, 2, 3])
    pass
