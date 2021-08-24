def my_solution(n):
    answer = ''

    while n is not 0:
        k = n % 3
        if k == 0:
            answer = '4' + answer
        elif k == 1:
            answer = '1' + answer
        else:
            answer = '2' + answer

        n = (n - 1) // 3

    return answer


def best_solution(n):
    # 출처 https://programmers.co.kr/learn/courses/30/lessons/12899/solution_groups?language=python3 / 지성인님
    num = ['1', '2', '4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer

# comment
"""
코드 내 의미상 차이는 한 가지로 볼 수 있는데, 본인은 if 문을 사용하여 나머지(0, 1, 2)에 해당하는 
숫자를 할당했지만, 지성인님께서는 list 내에 변수를 지정해놓고 인덱스로 찾았다는 점이 다르다.
"""

if __name__ == '__main__':
    pass
