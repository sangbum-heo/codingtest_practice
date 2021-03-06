# N : 1 ~ 500, 1 <= len(stages) <= 200,000 | stages[1 <= ? <= N+1]
# 실패율 높은 순으로 스테이지 내림차순 정렬

# stages index가 20만개까지 있을 수 있기 때문에 실행 시간 최적화

#딕셔너리 썼으면 좀 더 깔끔했겠다

N=5
stages=[2,1,2,6,2,4,3,3]

def solution(N, stages):
    answer = []
    num=[]
    stages.sort()
    for i in range(N):
        bunmo=0
        bunza=stages.count(i+1)
        num.append([])

        if stages.count(i+1) != 0:
            start = stages.index(i+1)
            bunmo = len(stages) - start
            num[i].append(bunza/bunmo)
            # stages.remove(i+1)  ← 시간 더 오래걸림
        else:
            num[i].append(0)
        num[i].append(i+1)
    
    num.sort(reverse=True)

    for i in range(N):
        for j in range(N):
            if (num[i][0] == num[j][0]) and (num[i][1] < num[j][1]): 
                num[i][1], num[j][1] = num[j][1], num[i][1]

    for i in range(N):
        answer.append(num[i][1])

    print(answer)
    return answer
solution(N, stages)