dartResult = "1D2S#10S"
def solution(dartResult):
    answer = 0
    tmp=[]
    scores=[]
    bonuses=[]
    options=[]
    i=0
    # dartResult 길이만큼 반복
    while i < len(dartResult):

        # index가 bonus 라면 
        if (dartResult[i] == 'S') or (dartResult[i] == 'D') or (dartResult[i] == 'T'):
            if dartResult[i] == 'S':
                bonuses.append(1)
            elif dartResult[i] == 'D':
                bonuses.append(2)
            else:
                bonuses.append(3)

            # 다음 index에 옵션이 없다면  (현재 index가 마지막 index) or (다음 index가 score라면)
            if i+1 == len(dartResult):
                options.append('')

            elif (dartResult[i+1] == '#') or (dartResult[i+1] == '*') :
                pass
            else:
                options.append('')

        # index가 '#' or '*' 이라면
        elif (dartResult[i] == '#') or (dartResult[i] == '*'):
            options.append(dartResult[i])

        # index가 score 라면
        elif (2 <= int(dartResult[i]) <= 9) or (int(dartResult[i]) == 0):
            scores.append(int(dartResult[i]))

        # index가 1이라면 다음 index가 0인지 확인, 다음 인덱스가 0이라면 10점 저장하고 i++ ( 다음으로 건너뛰기 )
        elif dartResult[i] == '1':
            if dartResult[i+1] == '0':
                scores.append(10)
                i+=1
            else:
                scores.append(1)
        i+=1

    for i in range(len(scores)):
        if options[i] == '#':
            tmp.append(scores[i] ** bonuses[i] * -1)
        elif options[i] == '':
            tmp.append(scores[i] ** bonuses[i])
        elif options[i] == '*':
            if i==0:
                tmp.append(scores[i] ** bonuses[i] * 2)
            else:
                tmp.append(scores[i] ** bonuses[i] * 2)
                tmp[i-1] = tmp[i-1] * 2
    
    answer=sum(tmp)

    print(answer)
    
    return answer

solution(dartResult)