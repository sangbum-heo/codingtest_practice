s="aabbaccc"

def solution(text): 
    if len(text) == 1: # len(text) == 1 ) 이 상황에서 예외처리 없이 정상작동하려면??? 음... 더 복잡해질거같고 굳이 해야하나 싶고.... 잘 모르겠다. 그래도 꽤나 최적화 성공했다
        return 1

    result2=[]

    for i in range(1,int(len(text)/2)+1):
        num=1
        front=""
        result=[]

        for j in range(0,len(text)+i,i): # 파이썬의 장점 ?? : s가 2글자일 때 print(s[0:10]) 이렇게 해도 오류가 안나고 마지막 문자까지 정상출력
            # 자리수가 딱 떨어지지 않을 때 마지막 요소 출력을 위한 +i, 슬라이싱 인덱스 넘어가도 오류 안난다
            if j == 0:
                front = text[j:j+i]
            else:
                if front == text[j:j+i]:
                    num+=1
                else:
                    if num == 1:
                        result.append(front)
                    else:
                        result.append(str(num)+front)
                    front = text[j:j+i]
                    num=1

        result2.append(sum(len(k) for k in result))

    answer = min(result2)
    return answer
solution(s)