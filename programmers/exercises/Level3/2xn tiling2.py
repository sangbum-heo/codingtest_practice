# n은 60000이하의 자연수
# def calc(n):

#     return n
arr=[1,2]
def solution(n):
    if(n <=2):
        return n
    
    count=n
    if (count > 2):
        solution(count-1)
        arr.append(arr[-2]+arr[-1])
    return arr[-1] % 1000000007

a = solution(20)

print("answer :",a)

