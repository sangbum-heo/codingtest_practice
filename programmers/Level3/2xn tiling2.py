# n은 60000이하의 자연수
# 재귀함수를 사용하니 정답은 나왔지만 효율성 테스트 통과 실패
import sys
# 파이썬의 재귀함수 호출 횟수 제한 60000으로 변경
sys.setrecursionlimit(60000)
arr=[1,2]
def solution(n):
    if(n <=2):
        return n
    
    count=n
    if (count > 2):
        solution(count-1)
        arr.append((arr[-2]+arr[-1]))
    return arr[-1] % 1000000007

a = solution(120)

print("answer :",a)

