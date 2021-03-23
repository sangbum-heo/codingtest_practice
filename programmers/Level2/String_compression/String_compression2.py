# x개씩 잘라서 append하고 -1번째랑 비교해서 같으면 몇번 반복되는지 저장 ㄱ
# s = "aabbaccc"


# 28개 테스트 중  1개 실패.   0.01ms만에 실패 뜸 짧은 문자열에서 문제 있는듯 len(s) == 1 이면 1 리턴하도록 고치긴 했는데

# floor(내림) 로 하지 말고 올림으로 하고 28/ 63 line 을 좀 바꾸면 굳이 1자리일때 1 리턴을 따로 만들지 않아도 괜찮지 않을까?

s = "aabbacc"

def solution(s):
    import math
    loop_count = math.floor(len(s)/2)
    result=[]
    result2=[]
    tmp=""
    answer = 0
    
    if len(s) == 1:
        print(1)
        return 1

    for i in range(loop_count):
        result.append([])
        s_index = 0
        for j in range(math.floor(len(s)/(i+1))):
            result[i].append(s[(i+1)*j:(i+1)*(j+1)])
        if(i+1)*(j+1) != len(s):
            result[i].append(s[(i+1)*(j+1):])
            
        result2.append([])
        num=1
        for j in range(math.floor(len(s)/(i+1))):

            # j가 마지막 번호라면
            if j == math.floor(len(s)/(i+1))-1:

                # 앞과 다르다면
                if result[i][j] != result[i][j-1]:
                    result2[i].append(result[i][j])

                # 앞과 같다면
                elif result[i][j] == result[i][j-1]:
                    result2[i].append(str(num)+result[i][j])
                    num=1

            # j가 마지막 번호가 아니라면
            else:
                # j가 앞과 같다면
                if result[i][j] == result[i][j+1]:
                    num+=1
                
                # j가 앞과 다르다면
                else:
                    # 이미 반복이 되었다면
                    if num != 1:
                        result2[i].append(str(num)+result[i][j])
                        num=1
                    else:
                        result2[i].append(result[i][j])

        # 마지막에 깔끔하게 떨어지지 않는 나머지 부분이 있다면 추가
        if(i+1)*(j+1) != len(s):
            result2[i].append(result[i][j+1])
    
    for i in result2:
        tmp=""
        if answer==0:
            for j in i:
                tmp+=j
                answer=len(tmp)
        else:
            for j in i:
                tmp += j
        if len(tmp) < answer:
            answer = len(tmp)
        

    print(answer)
    return answer

solution(s)