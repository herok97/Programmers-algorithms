import heapq


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].find(phone_book[i]) == 0:
            return False
    return True


# 출처: https://programmers.co.kr/learn/courses/30/lessons/42583/solution_groups?language=python3 김성식 외 111 명
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
"""
본인의 코드는 hash를 사용하지 않고 sort를 통해 연속적인 전화번호만 비교하는 코드로 직관적이다.
아래 다른 사람의 풀이를 보면 python에서 기본적으로 제공하는 dictionary 자료구조를 이용하였다.
기본적으로 이 자료구조는 hash map으로 구현되어 있어서 검색이 용이하다.
또한 한 가지 포인트는 dict.keys()를 이용하여 현재 전화번호와 나머지 전화번호를 모두 비교하게 되면
결국 list를 사용하는 것이기 때문에 복잡도가 크게 증가하게 될 것인데, 그렇지 않고 dict 자료구조를
그대로 이용하기 위해 현재 전화번호를 첫 글자부터 끊어서 dict 내에서 검색했다.
가장 빠른 속도로 구현된 코드로 보인다.
"""

if __name__ == '__main__':
    print(solution(["12", "123", "1235", "567", "88"]))
