dartResult="3D*10T#4S*"

def solution(dartResult):
    answer=[]

    dartResult=dartResult.replace("10","K")
    
    point = ["10" if i == "K" else i for i in dartResult]

    sdt = ['S','D','T']

    i = -1

    for j in point:
        if j in sdt:
            answer[i] **= (sdt.index(j)+1)
        elif j == '#':
            answer[i] *= -1
        elif j == '*':
            answer[i] *= 2
            if i != 0:
                answer[i-1] *= 2
        else:
            answer.append(int(j))
            i += 1

    print(sum(answer))

    return sum(answer)

solution(dartResult)