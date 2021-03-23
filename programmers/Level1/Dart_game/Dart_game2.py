dartResult = "1D*2S#10S*"

def solution(dartResult):

    answer=[]
    
    # 10은 index 2개를 차지하기 때문에 index 1개로 바꾸기 위해 10을 임시로 K로 변경
    dartResult = dartResult.replace('10','K')

    # i가 'K'라면 10을 넣고, 그게 아니라면 i를 넣는다.  이것을 dartResult 안에서 반복
    point=['10' if i == 'K' else i for i in dartResult]
    print(point)

    # i는 answer의 index  (숫자(score)가 있으면 answer의 index를 1 증가시키기 위해 i = -1로 초기화)
    i=-1

    # S는 1제곱, D는 2제곱, T는 3제곱이다. 그러므로 index + 1을 제곱해준다
    sdt=['S','D','T']

    # point의 원소 하나하나를 j를 통해 확인
    for j in point:
        if j in sdt:
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '#':
            answer[i] = answer[i] * -1
        elif j == '*':
            answer[i] = answer[i] * 2
            if i > 0:
                answer[i-1] = answer[i-1] * 2
        else:
            answer.append(int(j))
            i+=1

    return sum(answer)

solution(dartResult)