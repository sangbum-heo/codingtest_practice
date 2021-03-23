s="aabbaccc"

def solution(text):
    if len(text) == 1:
        return 1
    result3=[]
    for i in range(1,int(len(text)/2)+1):
        num=1
        front=""
        result=[]
        result2=0
        for j in range(0,int(len(text)),i):
            # print("i :",i,"/ j :",j,text[j:j+i])
            # text의 첫 번째 슬라이스면 front에 저장
            if j == 0:
                front = text[j:j+i]
            else:
                if front == text[j:j+i]:
                    num+=1
                else:
                    result.append([front,num])
                    front = text[j:j+i]
                    num=1
                if j+i >= int(len(text)):
                    result.append([front,num])
                    
        for q,w in result:
            if w == 1:
                result2+=len(q)
            else:
                result2+=len(q)+len(str(w))
        print(i,"result 2:",result2)
        result3.append(result2)

    answer = min(i for i in result3)
    print("answer :",answer)
    return answer
solution(s)