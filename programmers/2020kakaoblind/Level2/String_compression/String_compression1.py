# x개씩 잘라서 append하고 -1번째랑 비교해서 같으면 몇번 반복되는지 저장 ㄱ
s = "aabbaccc"


def solution(s):
    import math
    loop_count = math.floor(len(s)/2)
    result=[]
    result2=[]
    answer = 0
    num=0

    for i in range(loop_count):
        result.append([])
        for j in range(math.floor(len(s)/(i+1))):
            result[i].append(s[(i+1)*j:(i+1)*(j+1)])
        if(i+1)*(j+1) != len(s):
            result[i].append(s[(i+1)*(j+1):])
            
        result2.append([])

        for j in range(math.floor(len(s)/(i+1))):
            if j == 0:
                if result[i][j] != result[i][j+1]:
                    result2[i].append(result[i][j])
            else:
                if result[i][j] == result[i][j-1]:
                    num+=1
                    if j == math.floor(len(s)/(i+1))-1 or result[i][j] != result[i][j+1]:
                        next =str(num+1)+result[i][j]
                        result2[i].append(next)
                        num=0

                else:
                    result2[i].append(result[i][j])
                    # 2a 2b a 3c  로 나와야 하는데 a가 안나온다 ?

        if(i+1)*(j+1) != len(s):
            result2[i].append(result[i][j+1])
    print(result)
    print(result2)
    return answer

solution(s)